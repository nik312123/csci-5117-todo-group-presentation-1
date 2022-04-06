import re
from datetime import datetime
from typing import Union

from p0_nikunj_final.base_model import BaseModel
from p0_nikunj_final.user_model import UserModel


class TaskModel(BaseModel):
    __title_regex = re.compile(r"^[a-zA-Z0-9 ]+$")
    __color_format_regex = re.compile("^#[a-fA-F0-9]{6}$")
    __allowed_priorities = {"low", "medium", "high"}
    
    def __init__(self, data: Union[dict, str]):
        super().__init__(
            {"id", "title", "description", "dueDatetime", "user", "color", "priority", "isCompleted"}, data
        )
        
        self._validate_and_add_field(data, "id", int, TaskModel._validate_id)
        self._validate_and_add_field(data, "title", str, TaskModel._validate_title)
        self._validate_and_add_field(data, "description", str, TaskModel._validate_description)
        self._validate_and_add_field(data, "dueDatetime", object, TaskModel._validate_due_datetime)
        self._validate_and_add_field(data, "user", object, TaskModel._validate_user)
        self._validate_and_add_field(data, "color", str, TaskModel._validate_color)
        self._validate_and_add_field(data, "priority", str, TaskModel._validate_priority)
        self._validate_and_add_field(data, "isCompleted", bool)
    
    @classmethod
    def _validate_id(cls, task_id: int) -> int:
        if task_id <= 0:
            raise ValueError("The id must be positive.")
        return task_id
    
    @classmethod
    def _validate_title(cls, title: str) -> str:
        title = title.strip()
        
        title_len = len(title)
        if title_len < 1 or title_len > 30:
            raise ValueError("The title must be between 1 and 30 characters in length.")
        elif not cls.__title_regex.match(title):
            raise ValueError("The title must be composed only of alphanumeric characters and spaces.")
        return title
    
    @classmethod
    def _validate_description(cls, description: str) -> str:
        description = description.strip()
        
        if len(description) > 200:
            raise ValueError("The description must be at most 200 characters.")
        
        return description
    
    @classmethod
    def _validate_due_datetime(cls, due_datetime: Union[datetime, str]) -> datetime:
        if isinstance(due_datetime, str):
            try:
                due_datetime = datetime.fromisoformat(due_datetime)
            except ValueError:
                raise ValueError(
                    "The given string is not in the form YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]"
                )
        elif not isinstance(due_datetime, datetime):
            cls._raise_type_error("dueDatetime", "Union[datetime, str]", type(due_datetime).__name__)
        
        return due_datetime
    
    @classmethod
    def _validate_user(cls, user: Union[UserModel, dict]) -> UserModel:
        if isinstance(user, dict):
            user = UserModel(user)
        elif not isinstance(user, UserModel):
            cls._raise_type_error("user", "Union[dict, UserModel]", type(user).__name__)
        return user
    
    @classmethod
    def _validate_color(cls, color: str) -> str:
        if not cls.__color_format_regex.match(color):
            raise ValueError("The color should be a valid color hexadecimal string of length 7.")
        return color.upper()
    
    @classmethod
    def _validate_priority(cls, priority: str) -> str:
        if priority not in cls.__allowed_priorities:
            raise ValueError("The given priority must be low, medium, or high")
        return priority
