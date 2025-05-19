
from fastapi import FastAPI, Depends
from typing import List

from .database import init_db, reset_db, get_db
from .models import Task, TaskStatus, TaskType


app = FastAPI(title="Simulator API", openapi_url="/api/v1/openapi.json")

@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/api/v1/tasks/all", response_model=List[Task])
def get_tasks(from_date: str, to_date: str, conn=Depends(get_db)):
    cur = conn.execute(
        "SELECT * FROM tasks WHERE due_date BETWEEN ? AND ?",
        (from_date, to_date),
    )
    rows = cur.fetchall()
    return [Task(**dict(row)) for row in rows]


@app.post("/api/v1/sim/reset")
def reset_sim(seed: int | None = None):
    reset_db()
    return {"sim_date": "2025-05-12", "cleared": True}


@app.post("/api/v1/tasks/generate_daily")
def generate_daily(sim_date: str, conn=Depends(get_db)):
    tasks = []
    for _ in range(3):
        cur = conn.execute(
            "INSERT INTO tasks (type, vehicle_id, status, due_date, duration_min) VALUES (?,?,?,?,?)",
            (TaskType.monthly_check.value, None, TaskStatus.backlog.value, sim_date, 120),
        )
        tasks.append(cur.lastrowid)
    conn.commit()
    return {"generated": len(tasks)}


@app.get("/api/v1/tasks/backlog", response_model=List[Task])
def get_backlog(conn=Depends(get_db)):
    cur = conn.execute("SELECT * FROM tasks WHERE status = ?", (TaskStatus.backlog.value,))
    rows = cur.fetchall()
    return [Task(**dict(row)) for row in rows]
