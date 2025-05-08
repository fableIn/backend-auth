# FastAPI Backend Skeleton (v3)

A production‑ready FastAPI starter with:

* **JWT auth** – `/api/v1/login`
* **Registration** – `/api/v1/register`
* **Who‑am‑I** – `/api/v1/users/me`
* SQLAlchemy 2 + Alembic
* Pydantic 2 & pydantic‑settings
* Docker image based on `python:3.12‑slim`

## Quick start (local)

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Docker

```bash
# Build
docker build -t my-backend .

# Run (pass env vars via --env-file or individual -e)
docker run --env-file .env -p 8000:8000 my-backend
```

---
