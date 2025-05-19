# Simulator Skeleton

This repository contains an initial skeleton based on the provided specifications.

## Setup

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

## Endpoints

- `GET /api/v1/tasks/all?from=YYYY-MM-DD&to=YYYY-MM-DD`
- `POST /api/v1/sim/reset`
- `POST /api/v1/tasks/generate_daily`
- `GET /api/v1/tasks/backlog`

