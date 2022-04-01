import re
from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl, validator, constr, Field


class UserModel(BaseModel):
    email: EmailStr
    first_name: constr(min_length = 1, max_length = 30)
    has_middle_name: bool
    middle_name: Optional[constr(min_length = 1, max_length = 30)]
    last_name: constr(min_length = 1, max_length = 30)
    profile_url: Optional[HttpUrl] = Field(min_length = 13, max_length = 512)
    
    _name_format_regex = re.compile(r"^[a-zA-Z]$")
    
    @validator("email", "first_name", "middle_name", "last_name", "profile_url")
    def strip_spaces(cls, string: str) -> str:
        return string.strip()
    
    @validator("middle_name")
    def check_if_middle_name_should_be_included(cls, middle_name: Optional[str], values) -> Optional[str]:
        if values["has_middle_name"] and middle_name is None:
            raise ValueError("Checkbox picked for middle name but not middle name provided.")
        elif not values["has_middle_name"] and middle_name is not None:
            raise ValueError("Checkbox not picked for middle name but middle name provided")
        return middle_name
    
    @validator("first_name", "middle_name", "last_name")
    def check_name_part_format(cls, name_part: Optional[str]) -> Optional[str]:
        if name_part is None:
            return name_part
        if not cls._name_format_regex.match(name_part):
            raise ValueError("A name part may only consist of alphabetical characters")
        return name_part.capitalize()
