import os
import shutil
import zipfile
import subprocess
import time
import stat


def remove_tree_with_retries(path: str, retries: int = 5, delay_s: float = 1.0) -> None:
    """
    Windows can temporarily lock files/folders (e.g. __pycache__ under OneDrive).
    This makes cleanup for `lambda-package/` more resilient.
    """

    if not os.path.exists(path):
        return

    def onerror(func, p, exc_info):
        # Try to clear read-only bit then retry the failing op.
        try:
            os.chmod(p, stat.S_IWRITE)
            func(p)
        except Exception:
            pass

    for attempt in range(1, retries + 1):
        try:
            shutil.rmtree(path, onerror=onerror)
            return
        except PermissionError as e:
            if attempt == retries:
                break
            print(f"Warning: failed deleting {path} (attempt {attempt}/{retries}): {e}")
            time.sleep(delay_s)

    # Last resort: don't block deployments.
    shutil.rmtree(path, ignore_errors=True)


def remove_file_with_retries(path: str, retries: int = 5, delay_s: float = 1.0) -> None:
    if not os.path.exists(path):
        return

    for attempt in range(1, retries + 1):
        try:
            os.remove(path)
            return
        except PermissionError as e:
            if attempt == retries:
                break
            print(f"Warning: failed deleting {path} (attempt {attempt}/{retries}): {e}")
            time.sleep(delay_s)

    # Last resort
    try:
        os.remove(path)
    except Exception:
        pass


def main():
    print("Creating Lambda deployment package...")

    # Clean up
    if os.path.exists("lambda-package"):
        remove_tree_with_retries("lambda-package")
    if os.path.exists("lambda-deployment.zip"):
        remove_file_with_retries("lambda-deployment.zip")

    # Create package directory
    os.makedirs("lambda-package")

    # Install dependencies using Docker with Lambda runtime image
    print("Installing dependencies for Lambda runtime...")

    # Use the official AWS Lambda Python 3.12 image
    # This ensures compatibility with Lambda's runtime environment
    subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{os.getcwd()}:/var/task",
            "--platform",
            "linux/amd64",  # Force x86_64 architecture
            "--entrypoint",
            "",  # Override the default entrypoint
            "public.ecr.aws/lambda/python:3.12",
            "/bin/sh",
            "-c",
            "pip install --target /var/task/lambda-package -r /var/task/requirements.txt --platform manylinux2014_x86_64 --only-binary=:all: --upgrade",
        ],
        check=True,
    )

    # Copy application files
    print("Copying application files...")
    for file in ["server.py", "lambda_handler.py", "context.py", "resources.py"]:
        if os.path.exists(file):
            shutil.copy2(file, "lambda-package/")
    
    # Copy data directory
    if os.path.exists("data"):
        shutil.copytree("data", "lambda-package/data")

    # Create zip
    print("Creating zip file...")
    with zipfile.ZipFile("lambda-deployment.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk("lambda-package"):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, "lambda-package")
                zipf.write(file_path, arcname)

    # Show package size
    size_mb = os.path.getsize("lambda-deployment.zip") / (1024 * 1024)
    # Keep output ASCII-only for Windows terminals with cp1252 encoding.
    print(f"Created lambda-deployment.zip ({size_mb:.2f} MB)")


if __name__ == "__main__":
    main()