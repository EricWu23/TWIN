# Twin – Local Dev Notes

This repo contains:

- `backend/`: FastAPI API (Python)
- `frontend/`: Next.js UI (Node)
- `memory/`: local runtime artifacts (should not be committed)

## Quick start (Windows)

### Backend

From `twin/backend`:

```powershell
uv venv --python 3.12
uv sync
uv run uvicorn server:app --reload --port 8000
```

### Frontend

From `twin/frontend`:

```powershell
npm install
npm run dev
```

Open `http://localhost:3000`.

## What we learned (so far)

See `docs/LOCAL_DEV_WINDOWS.md`.

