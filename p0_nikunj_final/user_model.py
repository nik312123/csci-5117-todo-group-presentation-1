import re
from typing import Union, Optional

from email_validator import validate_email, EmailNotValidError

from p0_nikunj_final.base_model import BaseModel
from p0_nikunj_final.util import valid_url


class UserModel(BaseModel):
    __name_format_regex = re.compile(r"^[a-zA-Z]*$")
    
    def __init__(self, data: Union[dict, str]):
        super().__init__(
            {"email", "firstName", "hasMiddleName", "middleName", "lastName", "profileUrl"}, data, {"hasMiddleName"}
        )
        
        self._validate_and_add_field(data, "email", str, UserModel._validate_email)
        self._validate_and_add_field(data, "firstName", str, UserModel._validate_name_part)
        self._validate_and_add_field(data, "hasMiddleName", bool)
        self._validate_and_add_field_with_data(data, "middleName", object, UserModel._validate_middle_name, True)
        self._validate_and_add_field(data, "lastName", str, UserModel._validate_name_part)
        self._validate_and_add_field(data, "profileUrl", str, UserModel._validate_profile_url)
    
    @classmethod
    def _validate_email(cls, email: str) -> str:
        email = email.strip()
        try:
            validate_email(email, check_deliverability = False)
        except EmailNotValidError:
            raise ValueError("The provided email must be in an acceptable format.")
        return email
    
    @classmethod
    def _validate_name_part(cls, name_part: str) -> str:
        name_part = name_part.strip()
        
        name_part_len = len(name_part)
        if name_part_len < 1 or name_part_len > 30:
            raise ValueError("A name part must be between 1 and 30 characters in length.")
        
        if not cls.__name_format_regex.match(name_part):
            raise ValueError("A name part may only consist of alphabetical characters.")
        
        return name_part
    
    @classmethod
    def _validate_middle_name(cls, data: dict, middle_name: Optional[str]) -> Optional[str]:
        if middle_name is not None and not isinstance(middle_name, str):
            cls._raise_type_error("middleName", "Optional[None]", type(middle_name).__name__)
        
        if data["hasMiddleName"] and middle_name is None:
            raise ValueError("Checkbox picked for middle name but not middle name provided.")
        elif not data["hasMiddleName"] and middle_name is not None:
            raise ValueError("Checkbox not picked for middle name but middle name provided")
        
        if middle_name is None:
            return middle_name
        
        return cls._validate_name_part(middle_name)
    
    @classmethod
    def _validate_profile_url(cls, profile_url: str) -> str:
        if not valid_url(profile_url):
            raise ValueError("The profile URL must be a valid URL.")
        return profile_url
