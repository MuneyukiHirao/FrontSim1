from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    id: Optional[int]
    type: str
    vehicle_id: Optional[int]
    status: str
    due_date: str
    duration_min: int
    created_dt: str | None = None
