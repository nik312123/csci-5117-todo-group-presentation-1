from datetime import datetime
from typing import Literal

from pydantic import BaseModel, conint, constr, StrictBool
from pydantic.color import Color


class TaskModel(BaseModel):
    id: conint(gt = 0)
    title: constr(min_length = 1, max_length = 30, regex = r"^[a-zA-Z0-9 ]+$")
    description: constr(max_length = 200)
    due_datetime: datetime
    priority: Literal["low", "medium", "high"]
    is_completed: bool = False
    
    class Config:
        anystr_strip_whitespace = True
        validate_assignment = True
        orm_mode=True
