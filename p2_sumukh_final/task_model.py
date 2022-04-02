import re
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, validator, Field, StrictInt, StrictStr, StrictBool

from p2_sumukh_final.user_model import UserModel


class TaskModel(BaseModel):
    id: StrictInt
    title: StrictStr
    description: StrictStr
    due_datetime: datetime = Field(alias = "dueDatetime")
    user: UserModel
    color: StrictStr
    priority: Literal["low", "medium", "high"]
    is_completed: StrictBool = Field(False, alias = "isCompleted")
    
    # Underscores prevent fields from being part of the schema parsed by pydantic
    _title_format_regex = re.compile(r"^[a-zA-Z0-9 ]+$")
    _color_format_regex = re.compile("^#[a-fA-F0-9]{6}$")
    
    @validator("id")
    def check_id_is_positive(cls, task_id: int) -> int:
        if task_id <= 0:
            raise ValueError("The id must be positive.")
        return task_id
    
    @validator("title", "description", "color", "priority")
    def strip_spaces(cls, string: str) -> str:
        return string.strip()
    
    @validator("title")
    def check_title_length(cls, title: str) -> str:
        title_len = len(title)
        if title_len < 1 or title_len > 30:
            raise ValueError("The title must be between 1 and 30 characters in length.")
        return title
    
    @validator("title")
    def check_title_format(cls, title: str) -> str:
        if not cls._title_format_regex.match(title):
            raise ValueError("The title must be composed only of alphanumeric characters and spaces.")
        return title
    
    @validator("description")
    def check_description_length(cls, description: str) -> str:
        description_len = len(description)
        if description_len > 200:
            raise ValueError("The description must be at most 200 characters.")
        return description
    
    @validator("color")
    def check_color_format(cls, color: str) -> str:
        if not cls._color_format_regex.match(color):
            raise ValueError("The color should be a valid color hexadecimal string of length 7.")
        return color.upper()
