from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

from p1_siyad_final.user_model import UserModel


class TaskModel(BaseModel):
    id: int
    title: str
    description: str
    due_datetime: datetime = Field(alias = "dueDatetime")
    user: UserModel
    color: str
    priority: Literal["low", "medium", "high"]
    is_completed: bool = Field(False, alias = "isCompleted")
