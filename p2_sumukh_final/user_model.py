import re
from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl, validator, Field, StrictStr, StrictBool


class UserModel(BaseModel):
    email: EmailStr
    first_name: StrictStr = Field(alias = "firstName")
    has_middle_name: StrictBool = Field(alias = "hasMiddleName", exclude = True)
    middle_name: Optional[StrictStr] = Field(alias = "middleName")
    last_name: StrictStr = Field(alias = "lastName")
    profile_url: HttpUrl = Field(alias = "profileUrl")
    
    _name_format_regex = re.compile(r"^[a-zA-Z]*$")
    
    @validator("email", "first_name", "middle_name", "last_name", "profile_url")
    def strip_spaces(cls, string: Optional[str]) -> Optional[str]:
        if string is not None:
            return string.strip()
    
    @validator("middle_name")
    def check_if_middle_name_should_be_included(cls, middle_name: Optional[str], values) -> Optional[str]:
        if values["has_middle_name"] and middle_name is None:
            raise ValueError("Checkbox picked for middle name but not middle name provided.")
        elif not values["has_middle_name"] and middle_name is not None:
            raise ValueError("Checkbox not picked for middle name but middle name provided")
        return middle_name
    
    @validator("first_name", "middle_name", "last_name")
    def check_name_part_len(cls, name_part: Optional[str]) -> Optional[str]:
        if name_part is None:
            return name_part
        
        name_part_len = len(name_part)
        if name_part_len < 0 or name_part_len > 30:
            raise ValueError("A name part must be between 1 and 30 characters in length")
        return name_part
    
    @validator("first_name", "middle_name", "last_name")
    def check_name_part_format(cls, name_part: Optional[str]) -> Optional[str]:
        if name_part is None:
            return name_part
        if not cls._name_format_regex.match(name_part):
            raise ValueError("A name part may only consist of alphabetical characters")
        return name_part.capitalize()
    
    @validator("profile_url")
    def check_profile_url_length(cls, profile_url: HttpUrl) -> HttpUrl:
        profile_url_len = len(profile_url)
        if profile_url_len < 13 or profile_url_len > 512:
            raise ValueError("The profile URL length must be between 13 to 512 characters in length")
        return profile_url
    
    @validator("profile_url")
    def set_profile_url_to_string(cls, profile_url: HttpUrl) -> str:
        return str(profile_url)
