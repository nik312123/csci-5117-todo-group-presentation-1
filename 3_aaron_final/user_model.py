from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl, validator

from util import snake_case_to_camel_case


class UserModel(BaseModel):
    email: EmailStr
    fname: str
    has_mname: bool
    mname: Optional[str]
    lname: str
    profile_url: Optional[HttpUrl]
    
    class Config:
        anystr_strip_whitespace = True
        allow_mutation = False
        alias_generator = snake_case_to_camel_case
        min_anystr_length = 1
        max_anystr_length = 30
        fields = {
            "has_mname": {
                "exclude": True
            }
        }
    
    @validator("mname")
    def check_if_mname_should_be_included(cls, mname: Optional[str], values) -> Optional[str]:
        if values["has_mname"] and mname is None:
            raise ValueError("Checkbox picked for middle name but not middle name provided.")
        elif not values["has_mname"] and mname is not None:
            raise ValueError("Checkbox not picked for middle name but middle name provided")
        return mname
    
    @validator("fname", "mname", "lname")
    def replace_spaces_in_name_part_with_underscores(cls, name_part: str) -> str:
        return name_part.replace(" ", "_")
    
    @validator("profile_url")
    def check_if_profile_url_length_is_valid(cls, profile_url: Optional[HttpUrl]) -> Optional[HttpUrl]:
        if profile_url is None:
            return profile_url
        elif len(profile_url) < 13 or len(profile_url) > 512:
            raise ValueError("The length of the profile URL must be between 13 and 512 characters.")
