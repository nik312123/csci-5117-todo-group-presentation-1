from datetime import datetime
from typing import Literal

from pydantic import BaseModel, conint, constr, color, validator

from user_model import UserModel


class TaskModel(BaseModel):
    id: conint(gt = 0)
    title: constr(min_length = 1, max_length = 30, strip_whitespace = True, regex = r"^[a-zA-Z0-9 ]+$")
    description: constr(max_length = 200, strip_whitespace = True)
    due_datetime: datetime
    user: UserModel
    color: color.Color
    priority: Literal["low", "medium", "high"]
    is_completed: bool = False
    
    @validator("title", "description")
    def strip_spaces(cls, string: str) -> str:
        return string.strip()
