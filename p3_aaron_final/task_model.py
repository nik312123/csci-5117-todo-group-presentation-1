"""
Aaron, make sure to have strip_whitespace = True initially for both the title and description before going into config.
"""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, validator, conint, constr
from pydantic.color import Color

from p3_aaron_final.user_model import UserModel
from p3_aaron_final.util import snake_case_to_camel_case


class TaskModel(BaseModel):
    id: conint(gt = 0, strict = True)
    title: constr(min_length = 1, max_length = 30, regex = r"^[a-zA-Z0-9 ]+$", strict = True)
    description: constr(max_length = 200, strict = True)
    due_datetime: datetime
    user: UserModel
    color: Color
    priority: Literal["low", "medium", "high"]
    is_completed: bool = False
    
    class Config:
        anystr_strip_whitespace = True
        validate_assignment = True
        alias_generator = snake_case_to_camel_case
