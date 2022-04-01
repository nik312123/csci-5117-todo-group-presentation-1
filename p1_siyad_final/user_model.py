import re
from typing import Optional

from email_validator import validate_email, EmailNotValidError
from pydantic import BaseModel, validator, Field

from p1_siyad_final.util import valid_url


class UserModel(BaseModel):
    email: str
    first_name: str = Field(alias = "firstName")
    has_middle_name: bool = Field(alias = "hasMiddleName")
    middle_name: Optional[str] = Field(alias = "middleName")
    last_name: str = Field(alias = "lastName")
    profile_url: str = Field(alias = "profileUrl")
    
    _name_format_regex = re.compile(r"^[a-zA-Z]+$")
    
    @validator("email", "first_name", "middle_name", "last_name", "profile_url")
    def strip_spaces(cls, string: str) -> str:
        return string.strip()
    
    @validator("email")
    def check_email_format(cls, email: str) -> str:
        try:
            validate_email(email, check_deliverability = False)
            return email
        except EmailNotValidError:
            raise ValueError("The provided email must be in an acceptable format.")
    
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
    def check_profile_url_length(cls, profile_url: str) -> str:
        profile_url_len = len(profile_url)
        if profile_url_len < 13 or profile_url_len > 512:
            raise ValueError("The profile URL length must be between 13 to 512 characters in length")
        return profile_url
    
    @validator("profile_url")
    def check_profile_url_format(cls, profile_url: str) -> str:
        if not valid_url(profile_url):
            raise ValueError("The profile URL must be a valid URL")
        return profile_url
