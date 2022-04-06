from datetime import datetime
from typing import Literal

from pydantic import BaseModel, conint, constr
from pydantic.color import Color

from p4_sumanth_final.util import snake_case_to_camel_case


class TaskModel(BaseModel):
    id: conint(gt = 0)
    title: constr(min_length = 1, max_length = 30, regex = r"^[a-zA-Z0-9 ]+$")
    description: constr(max_length = 200)
    due_datetime: datetime
    email: str
    color: Color
    priority: Literal["low", "medium", "high"]
    is_completed: bool = False
    
    class Config:
        anystr_strip_whitespace = True
        validate_assignment = True
        alias_generator = snake_case_to_camel_case
        orm_mode = True
        allow_population_by_field_name = True
