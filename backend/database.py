import sqlite3
from contextlib import contextmanager
from pathlib import Path

DB_PATH = Path("./data/sim.db")


def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                vehicle_id INTEGER,
                status TEXT,
                due_date TEXT,
                duration_min INTEGER,
                created_dt TEXT DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
            )
            """
        )
        conn.commit()


def reset_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DROP TABLE IF EXISTS tasks")
    init_db()


@contextmanager
def get_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        yield conn

