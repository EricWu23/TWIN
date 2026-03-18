# Local development (Windows) – Learnings

This document captures the issues hit during local testing on Windows and how we fixed them.

## Backend (Python + uv)

### Symptom

Running `uv add -r requirements.txt` failed with an error like:

- `Querying Python at ...\.venv\Scripts\python.exe failed`
- `No Python at '"C:\Python312\python.exe"'`

### Root cause

`backend/.venv/pyvenv.cfg` had:

- `home = C:\Python312`

but Windows did not have Python installed there. `uv` will try to reuse the existing `.venv`, so it kept pointing at a non-existent interpreter.

### Fix

Recreate the venv using a real Python 3.12 interpreter.

From `backend/`:

```powershell
Remove-Item -Recurse -Force .venv
uv venv --python 3.12
uv sync
```

Verify:

```powershell
uv run python --version
```

### Notes

- `backend/.python-version` pins `3.12` and `backend/pyproject.toml` has `requires-python = ">=3.12"`.
- Prefer `uv sync` (uses `pyproject.toml`) over `uv add -r requirements.txt` for this repo.

## Frontend (Next.js Turbopack on OneDrive)

### Symptom

`npm run dev` crashed immediately with:

- `Error [TurbopackInternalError]: Access is denied. (os error 5)`

and wrote a “panic log” under `%TEMP%` like:

- `C:\Users\<you>\AppData\Local\Temp\next-panic-....log`

### Why it happens

On Windows, Turbopack can hit permission/file-lock issues when the project lives under OneDrive (sync), or when antivirus/Defender scans/locks files. Turbopack writes/renames/watches files in `.next` very rapidly, so it’s more sensitive to locks.

### Fix (recommended)

Disable Turbopack for local development and use Webpack instead.

This repo sets:

- `frontend/package.json` `dev` script → `next dev --webpack`

Then from `frontend/`:

```powershell
Remove-Item -Recurse -Force .next
npm run dev
```

### Alternative fixes

- Move the repo outside OneDrive (e.g. `C:\dev\twin`)
- Exclude the project folder from OneDrive sync / antivirus scanning (if permitted)

