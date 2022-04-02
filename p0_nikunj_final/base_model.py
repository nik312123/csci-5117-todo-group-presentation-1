import json
from copy import deepcopy
from typing import Any, Callable, Optional, Set, Type, Union


class BaseModel:
    
    def __init__(self, valid_fieldnames: Set[str], data: Union[dict, str], fields_to_exclude: Set[str] = None):
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                raise ValueError("The provided string is not valid JSON.")
        elif not isinstance(data, dict):
            raise ValueError("The provided data must be either a JSON string or a dict.")
        
        for field_name in data:
            if field_name not in valid_fieldnames:
                raise ValueError(f"Field {field_name} is not one of the permitted fields.")
        
        self.__model = {}
        
        if fields_to_exclude is None:
            fields_to_exclude = set()
        self.__fields_to_exclude = fields_to_exclude.copy()
    
    class BaseModelEncoder(json.JSONEncoder):
        def default(self, o: Any) -> Any:
            if isinstance(o, BaseModel):
                return o.to_dict()
            return super().default(o)
    
    @classmethod
    def _raise_type_error(cls, field_name: str, expected_type: str, actual_type: str) -> None:
        raise TypeError(
            f"Field {field_name} was expected to be of type {expected_type}."
            f" Was actually of type {actual_type}."
        )
    
    def _validate_and_add_field(
        self, data: dict, field_name: str, field_type: Type,
        validate_field: Callable[[Any], Any] = lambda field_value: field_value, default_enabled: bool = False,
        default_value: Any = None) -> None:
        if field_name not in data and not default_enabled:
            raise ValueError(f"Required field {field_name} is missing from the provided data.")
        elif default_enabled and field_name not in data:
            value = default_value
        else:
            value = data[field_name]
        
        if field_type == int and isinstance(value, bool):
            self._raise_type_error(field_name, field_type.__name__, type(value).__name__)
        elif not isinstance(value, field_type):
            self._raise_type_error(field_name, field_type.__name__, type(value).__name__)
        
        self.__model[field_name] = validate_field(value)
    
    def _validate_and_add_field_with_data(
        self, data: dict, field_name: str, field_type: Type, validate_field: Callable[[dict, Any], None],
        default_enabled: bool = False, default_value: Any = None) -> None:
        self._validate_and_add_field(
            data, field_name, field_type, lambda field_value: validate_field(data, field_value), default_enabled,
            default_value
        )
    
    def get(self, field_name: str) -> Any:
        return self.__model[field_name]
    
    def get_default(self, field_name: str, default: Any = None) -> Optional[Any]:
        return self.__model.get(field_name, default)
    
    def to_dict(self) -> dict:
        model_dict = deepcopy(self.__model)
        
        for key, value in model_dict.items():
            if isinstance(value, BaseModel):
                model_dict[key] = value.to_dict()
        
        for field in self.__fields_to_exclude:
            model_dict.pop(field)
        return model_dict
    
    def to_json(self) -> str:
        model_dict = self.__model.copy()
        for field in self.__fields_to_exclude:
            model_dict.pop(field)
        return json.dumps(self.__model, cls = BaseModel.BaseModelEncoder)
