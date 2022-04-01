"""
Aaron, don't forget to start with constr implementation before using min_anystr_length and max_anystr_length.
Aaron, make sure to have strip_whitespace = True initially for the name parts before going into config.
"""

import re
from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl, validator, Field

from p3_aaron_final.util import snake_case_to_camel_case


class UserModel(BaseModel):
    email: EmailStr
    first_name: str
    has_middle_name: bool
    middle_name: Optional[str]
    last_name: str
    profile_url: HttpUrl = Field(min_length = 13, max_length = 512)
    
    _name_format_regex = re.compile(r"^[a-zA-Z]$")
    
    class Config:
        anystr_strip_whitespace = True
        allow_mutation = False
        alias_generator = snake_case_to_camel_case
        min_anystr_length = 1
        max_anystr_length = 30
        fields = {
            "has_middle_name": {
                "exclude": True
            }
        }
    
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
