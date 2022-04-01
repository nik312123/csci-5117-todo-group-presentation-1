from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl, validator, constr


class UserModel(BaseModel):
    email: EmailStr
    first_name: constr(min_length = 1, max_length = 30)
    has_middle_name: bool
    middle_name: Optional[constr(min_length = 1, max_length = 30)]
    last_name: constr(min_length = 1, max_length = 30)
    profile_url: Optional[HttpUrl]
    
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
    def replace_spaces_in_name_part_with_underscores(cls, name_part: str) -> str:
        return name_part.replace(" ", "_")
    
    @validator("profile_url")
    def check_if_profile_url_length_is_valid(cls, profile_url: Optional[HttpUrl]) -> Optional[HttpUrl]:
        if profile_url is None:
            return profile_url
        elif len(profile_url) < 13 or len(profile_url) > 512:
            raise ValueError("The length of the profile URL must be between 13 and 512 characters.")
