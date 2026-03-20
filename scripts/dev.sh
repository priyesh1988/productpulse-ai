#!/usr/bin/env bash
set -euo pipefail

docker compose up -d postgres qdrant redis
(
  cd backend
  python -m venv .venv || true
  source .venv/bin/activate
  pip install -r requirements.txt
  uvicorn app.main:app --reload --port 8000
) &
(
  cd frontend
  npm install
  npm run dev
)
