from fastapi import FastAPI
from typing import List

from .database import get_conn, init_db
from .models import Task

app = FastAPI(title="Simulator API", openapi_url="/api/v1/openapi.json")

@app.on_event("startup")
def startup():
    init_db()


@app.get("/api/v1/tasks/all", response_model=List[Task])
def get_tasks(from_date: str, to_date: str):
    query = "SELECT * FROM tasks WHERE due_date BETWEEN ? AND ?"
    with get_conn() as conn:
        rows = conn.execute(query, (from_date, to_date)).fetchall()
        return [Task(**dict(row)) for row in rows]


@app.post("/api/v1/sim/reset")
def reset_sim(seed: int | None = None):
    with get_conn() as conn:
        conn.execute("DROP TABLE IF EXISTS tasks")
    init_db()
    return {"sim_date": "2025-05-12", "cleared": True}
