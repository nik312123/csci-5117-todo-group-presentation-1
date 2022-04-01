from datetime import datetime
from typing import Literal

from pydantic import BaseModel, conint, constr, color

from user_model import UserModel
from util import snake_case_to_camel_case


class TaskModel(BaseModel):
    id: conint(gt = 0)
    title: constr(min_length = 1, max_length = 30, strip_whitespace = True, regex = r"^[a-zA-Z0-9 ]+$")
    description: constr(max_length = 200, strip_whitespace = True)
    due_datetime: datetime
    user: UserModel
    color: color.Color
    priority: Literal["low", "medium", "high"]
    is_completed: bool = False
    
    class Config:
        anystr_strip_whitespace = True
        validate_assignment = True
        alias_generator = snake_case_to_camel_case
