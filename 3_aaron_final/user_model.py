"""
Aaron, don't forget to start with constr implementation before using min_anystr_length and max_anystr_length.
"""

from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl, validator

from util import snake_case_to_camel_case


class UserModel(BaseModel):
    email: EmailStr
    first_name: str
    has_middle_name: bool
    middle_name: Optional[str]
    last_name: str
    profile_url: Optional[HttpUrl]
    
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
    def replace_spaces_in_name_part_with_underscores(cls, name_part: str) -> str:
        return name_part.replace(" ", "_")
    
    @validator("profile_url")
    def check_if_profile_url_length_is_valid(cls, profile_url: Optional[HttpUrl]) -> Optional[HttpUrl]:
        if profile_url is None:
            return profile_url
        elif len(profile_url) < 13 or len(profile_url) > 512:
            raise ValueError("The length of the profile URL must be between 13 and 512 characters.")
