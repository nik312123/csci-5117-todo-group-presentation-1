from typing import Optional

from pydantic import BaseModel, Field


class UserModel(BaseModel):
    email: str
    first_name: str = Field(alias = "firstName")
    has_middle_name: bool = Field(alias = "hasMiddleName")
    middle_name: Optional[str] = Field(alias = "middleName")
    last_name: str = Field(alias = "lastName")
    profile_url: str = Field(alias = "profileUrl")
