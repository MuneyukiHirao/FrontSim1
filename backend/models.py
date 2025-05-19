from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from datetime import datetime


class TaskStatus(str, Enum):
    backlog = "backlog"
    unassigned = "unassigned"
    tentative = "tentative"
    assigned = "assigned"
    done = "done"


class TaskType(str, Enum):
    contract_maint = "contract_maint"
    monthly_check = "monthly_check"
    new_machine = "new_machine"
    sales_lead = "sales_lead"
    customer_req = "customer_req"


@dataclass
class Task:
    id: int | None
    type: TaskType
    vehicle_id: int | None
    status: TaskStatus
    due_date: str
    duration_min: int
    created_dt: str
