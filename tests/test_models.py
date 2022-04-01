from copy import deepcopy
from datetime import datetime
from typing import Type

import pytest
from pydantic import ValidationError
from pydantic.color import Color

from p1_siyad_final.task_model import TaskModel as P1TaskModel
from p2_sumukh_final.task_model import TaskModel as P2TaskModel
from p3_aaron_final.task_model import TaskModel as P3TaskModel

correct_task_with_no_middle_name_with_field = {
    "id": 1,
    "title": "Hello Goodbye 7 l33t",
    "description": "This task is obviously about hello goodbye 7 l33t. What more do you need?",
    "dueDatetime": datetime(2022, 3, 31, 11, 32, 10),
    "user": {
        "email": "chawl025@umn.edu",
        "firstName": "Nikunj",
        "hasMiddleName": False,
        "middleName": None,
        "lastName": "Chawla",
        "profileUrl": "https://github.com/nik312123"
    },
    "color": "#0197F6",
    "priority": "low",
    "isCompleted": False
}

correct_task_with_no_middle_name_without_field = {
    "id": 1,
    "title": "Hello Goodbye 7 l33t",
    "description": "This task is obviously about hello goodbye 7 l33t. What more do you need?",
    "dueDatetime": datetime(2022, 3, 31, 11, 32, 10),
    "user": {
        "email": "chawl025@umn.edu",
        "firstName": "Nikunj",
        "hasMiddleName": False,
        "lastName": "Chawla",
        "profileUrl": "https://github.com/nik312123"
    },
    "color": "#0197F6",
    "priority": "low",
    "isCompleted": False
}

# noinspection SpellCheckingInspection
correct_task_with_middle_name = {
    "id": 1,
    "title": "Hello Goodbye 7 l33t",
    "description": "This task is obviously about hello goodbye 7 l33t. What more do you need?",
    "dueDatetime": datetime(2022, 3, 31, 11, 32, 10),
    "user": {
        "email": "chawl025@umn.edu",
        "firstName": "Nikunj",
        "hasMiddleName": True,
        "middleName": "Chanik",
        "lastName": "Chawla",
        "profileUrl": "https://github.com/nik312123"
    },
    "color": "#0197F6",
    "priority": "low",
    "isCompleted": False
}

incorrect_task_with_negative_id = {
    "id": -1,
    "title": "Hello Goodbye 7 l33t",
    "description": "This task is obviously about hello goodbye 7 l33t. What more do you need?",
    "dueDatetime": datetime(2022, 3, 31, 11, 32, 10),
    "user": {
        "email": "chawl025@umn.edu",
        "firstName": "Nikunj",
        "hasMiddleName": False,
        "middleName": None,
        "lastName": "Chawla",
        "profileUrl": "https://github.com/nik312123"
    },
    "color": "#0197F6",
    "priority": "low",
    "isCompleted": False
}

incorrect_task_with_zero_id = {
    "id": 0,
    "title": "Hello Goodbye 7 l33t",
    "description": "This task is obviously about hello goodbye 7 l33t. What more do you need?",
    "dueDatetime": datetime(2022, 3, 31, 11, 32, 10),
    "user": {
        "email": "chawl025@umn.edu",
        "firstName": "Nikunj",
        "hasMiddleName": False,
        "middleName": None,
        "lastName": "Chawla",
        "profileUrl": "https://github.com/nik312123"
    },
    "color": "#0197F6",
    "priority": "low",
    "isCompleted": False
}

incorrect_task_with_incorrectly_typed_id = {
    "id": True,
    "title": "Hello Goodbye 7 l33t",
    "description": "This task is obviously about hello goodbye 7 l33t. What more do you need?",
    "dueDatetime": datetime(2022, 3, 31, 11, 32, 10),
    "user": {
        "email": "chawl025@umn.edu",
        "firstName": "Nikunj",
        "hasMiddleName": False,
        "middleName": None,
        "lastName": "Chawla",
        "profileUrl": "https://github.com/nik312123"
    },
    "color": "#0197F6",
    "priority": "low",
    "isCompleted": False
}

incorrect_task_with_empty_title = {
    "id": 1,
    "title": "",
    "description": "This task is obviously about hello goodbye 7 l33t. What more do you need?",
    "dueDatetime": datetime(2022, 3, 31, 11, 32, 10),
    "user": {
        "email": "chawl025@umn.edu",
        "firstName": "Nikunj",
        "hasMiddleName": False,
        "middleName": None,
        "lastName": "Chawla",
        "profileUrl": "https://github.com/nik312123"
    },
    "color": "#0197F6",
    "priority": "low",
    "isCompleted": False
}

incorrect_task_with_too_long_title = {
    "id": 1,
    "title": "Anna ate an apple and applauded",
    "description": "This task is obviously about hello goodbye 7 l33t. What more do you need?",
    "dueDatetime": datetime(2022, 3, 31, 11, 32, 10),
    "user": {
        "email": "chawl025@umn.edu",
        "firstName": "Nikunj",
        "hasMiddleName": False,
        "middleName": None,
        "lastName": "Chawla",
        "profileUrl": "https://github.com/nik312123"
    },
    "color": "#0197F6",
    "priority": "low",
    "isCompleted": False
}

incorrect_task_with_malformatted_title = {
    "id": 1,
    "title": "Hello. Goodbye 7 l33t",
    "description": "This task is obviously about hello goodbye 7 l33t. What more do you need?",
    "dueDatetime": datetime(2022, 3, 31, 11, 32, 10),
    "user": {
        "email": "chawl025@umn.edu",
        "firstName": "Nikunj",
        "hasMiddleName": False,
        "middleName": None,
        "lastName": "Chawla",
        "profileUrl": "https://github.com/nik312123"
    },
    "color": "#0197F6",
    "priority": "low",
    "isCompleted": False
}

incorrect_task_with_incorrectly_typed_title = {
    "id": 1,
    "title": 9,
    "description": "This task is obviously about hello goodbye 7 l33t. What more do you need?",
    "dueDatetime": datetime(2022, 3, 31, 11, 32, 10),
    "user": {
        "email": "chawl025@umn.edu",
        "firstName": "Nikunj",
        "hasMiddleName": False,
        "middleName": None,
        "lastName": "Chawla",
        "profileUrl": "https://github.com/nik312123"
    },
    "color": "#0197F6",
    "priority": "low",
    "isCompleted": False
}

incorrect_task_with_too_long_description = {
    "id": 1,
    "title": "Hello Goodbye 7 l33t",
    "description": "a" * 201,
    "dueDatetime": datetime(2022, 3, 31, 11, 32, 10),
    "user": {
        "email": "chawl025@umn.edu",
        "firstName": "Nikunj",
        "hasMiddleName": False,
        "middleName": None,
        "lastName": "Chawla",
        "profileUrl": "https://github.com/nik312123"
    },
    "color": "#0197F6",
    "priority": "low",
    "isCompleted": False
}

incorrect_task_with_incorrectly_typed_description = {
    "id": 1,
    "title": "Hello Goodbye 7 l33t",
    "description": 7,
    "dueDatetime": datetime(2022, 3, 31, 11, 32, 10),
    "user": {
        "email": "chawl025@umn.edu",
        "firstName": "Nikunj",
        "hasMiddleName": False,
        "middleName": None,
        "lastName": "Chawla",
        "profileUrl": "https://github.com/nik312123"
    },
    "color": "#0197F6",
    "priority": "low",
    "isCompleted": False
}

correct_task_with_valid_datetime_string = {
    "id": 1,
    "title": "Hello Goodbye 7 l33t",
    "description": "This task is obviously about hello goodbye 7 l33t. What more do you need?",
    "dueDatetime": "2022-03-31 11:59:59",
    "user": {
        "email": "chawl025@umn.edu",
        "firstName": "Nikunj",
        "hasMiddleName": False,
        "middleName": None,
        "lastName": "Chawla",
        "profileUrl": "https://github.com/nik312123"
    },
    "color": "#0197F6",
    "priority": "low",
    "isCompleted": False
}

incorrect_task_with_unsupported_datetime_string = {
    "id": 1,
    "title": "Hello Goodbye 7 l33t",
    "description": "This task is obviously about hello goodbye 7 l33t. What more do you need?",
    "dueDatetime": "2022/03/31 11:59:59",
    "user": {
        "email": "chawl025@umn.edu",
        "firstName": "Nikunj",
        "hasMiddleName": False,
        "middleName": None,
        "lastName": "Chawla",
        "profileUrl": "https://github.com/nik312123"
    },
    "color": "#0197F6",
    "priority": "low",
    "isCompleted": False
}

def assert_model_dicts_equal(task_dict: dict, expected_dict: dict) -> None:
    assert task_dict["id"] == expected_dict["id"]
    assert task_dict["title"] == expected_dict["title"]
    assert task_dict["description"] == expected_dict["description"]
    assert task_dict["dueDatetime"] == expected_dict["dueDatetime"]
    assert task_dict["user"]["email"] == expected_dict["user"]["email"]
    assert task_dict["user"]["firstName"] == expected_dict["user"]["firstName"]
    assert task_dict["user"]["middleName"] == expected_dict["user"]["middleName"]
    assert task_dict["user"].get("hasMiddleName") == expected_dict["user"].get("hasMiddleName")
    assert task_dict["user"]["lastName"] == expected_dict["user"]["lastName"]
    assert task_dict["user"]["profileUrl"] == expected_dict["user"]["profileUrl"]
    if isinstance(task_dict["color"], Color):
        assert task_dict["color"].as_hex() == expected_dict["color"].as_hex()
    else:
        assert task_dict["color"] == expected_dict["color"]
    assert task_dict["priority"] == expected_dict["priority"]
    assert task_dict["isCompleted"] == expected_dict["isCompleted"]


def convert_to_p2_expected_dict(expected_dict: dict) -> None:
    expected_dict["user"].pop("hasMiddleName")


def convert_to_p3_expected_dict(expected_dict: dict) -> None:
    convert_to_p2_expected_dict(expected_dict)
    expected_dict["color"] = Color(expected_dict["color"])


def test_correct_task_with_no_middle_name_with_field_p1() -> None:
    task = P1TaskModel(**correct_task_with_no_middle_name_with_field)
    assert_model_dicts_equal(task.dict(by_alias = True), correct_task_with_no_middle_name_with_field)


def test_correct_task_with_no_middle_name_with_field_p2() -> None:
    task = P2TaskModel(**correct_task_with_no_middle_name_with_field)
    expected_dict = deepcopy(correct_task_with_no_middle_name_with_field)
    convert_to_p2_expected_dict(expected_dict)
    assert_model_dicts_equal(task.dict(by_alias = True), expected_dict)


def test_correct_task_with_no_middle_name_with_field_p3() -> None:
    task = P3TaskModel(**correct_task_with_no_middle_name_with_field)
    expected_dict = deepcopy(correct_task_with_no_middle_name_with_field)
    convert_to_p3_expected_dict(expected_dict)
    assert_model_dicts_equal(task.dict(by_alias = True), expected_dict)


def test_correct_task_with_no_middle_name_without_field_p1() -> None:
    task = P1TaskModel(**correct_task_with_no_middle_name_without_field)
    expected_dict = deepcopy(correct_task_with_no_middle_name_without_field)
    # noinspection PyTypeChecker
    expected_dict["user"]["middleName"] = None
    assert_model_dicts_equal(task.dict(by_alias = True), expected_dict)


def test_correct_task_with_no_middle_name_without_field_p2() -> None:
    task = P2TaskModel(**correct_task_with_no_middle_name_without_field)
    expected_dict = deepcopy(correct_task_with_no_middle_name_without_field)
    # noinspection PyTypeChecker
    expected_dict["user"]["middleName"] = None
    convert_to_p2_expected_dict(expected_dict)
    assert_model_dicts_equal(task.dict(by_alias = True), expected_dict)


def test_correct_task_with_no_middle_name_without_field_p3() -> None:
    task = P3TaskModel(**correct_task_with_no_middle_name_without_field)
    expected_dict = deepcopy(correct_task_with_no_middle_name_without_field)
    # noinspection PyTypeChecker
    expected_dict["user"]["middleName"] = None
    convert_to_p3_expected_dict(expected_dict)
    assert_model_dicts_equal(task.dict(by_alias = True), expected_dict)


def test_correct_task_with_middle_name_p1() -> None:
    task = P1TaskModel(**correct_task_with_middle_name)
    assert_model_dicts_equal(task.dict(by_alias = True), correct_task_with_middle_name)


def test_correct_task_with_middle_name_p2() -> None:
    task = P2TaskModel(**correct_task_with_middle_name)
    expected_dict = deepcopy(correct_task_with_middle_name)
    convert_to_p2_expected_dict(expected_dict)
    assert_model_dicts_equal(task.dict(by_alias = True), expected_dict)


def test_correct_task_with_middle_name_p3() -> None:
    task = P3TaskModel(**correct_task_with_middle_name)
    expected_dict = deepcopy(correct_task_with_middle_name)
    convert_to_p3_expected_dict(expected_dict)
    assert_model_dicts_equal(task.dict(by_alias = True), expected_dict)


def check_incorrect_task_one_error(
    task_model_class: Type, input_dict: dict, message: str) -> None:
    with pytest.raises(ValidationError) as e_info:
        task_model_class(**input_dict)
    e = e_info.value
    assert len(e.errors()) == 1
    assert e.errors()[0]["msg"] == message


def test_incorrect_task_with_negative_id_p1() -> None:
    check_incorrect_task_one_error(P1TaskModel, incorrect_task_with_negative_id, "The id must be positive.")


def test_incorrect_task_with_negative_id_p2() -> None:
    check_incorrect_task_one_error(P2TaskModel, incorrect_task_with_negative_id, "The id must be positive.")


def test_incorrect_task_with_negative_id_p3() -> None:
    check_incorrect_task_one_error(P3TaskModel, incorrect_task_with_negative_id, "ensure this value is greater than 0")


def test_incorrect_task_with_zero_id_p1() -> None:
    check_incorrect_task_one_error(P1TaskModel, incorrect_task_with_zero_id, "The id must be positive.")


def test_incorrect_task_with_zero_id_p2() -> None:
    check_incorrect_task_one_error(P2TaskModel, incorrect_task_with_zero_id, "The id must be positive.")


def test_incorrect_task_with_zero_id_p3() -> None:
    check_incorrect_task_one_error(P3TaskModel, incorrect_task_with_zero_id, "ensure this value is greater than 0")


# No such typed test exists for p1 as strict typing is not introduced


def test_incorrect_task_with_incorrectly_typed_id_p2() -> None:
    check_incorrect_task_one_error(
        P2TaskModel, incorrect_task_with_incorrectly_typed_id, "value is not a valid integer"
    )


def test_incorrect_task_with_incorrectly_typed_id_p3() -> None:
    check_incorrect_task_one_error(
        P3TaskModel, incorrect_task_with_incorrectly_typed_id, "value is not a valid integer"
    )


def test_incorrect_task_with_empty_title_p1() -> None:
    check_incorrect_task_one_error(
        P1TaskModel, incorrect_task_with_empty_title, "The title must be between 1 and 30 characters in length."
    )


def test_incorrect_task_with_empty_title_p2() -> None:
    check_incorrect_task_one_error(
        P2TaskModel, incorrect_task_with_empty_title, "The title must be between 1 and 30 characters in length."
    )


def test_incorrect_task_with_empty_title_p3() -> None:
    check_incorrect_task_one_error(
        P3TaskModel, incorrect_task_with_empty_title, "ensure this value has at least 1 characters"
    )


def test_incorrect_task_with_too_long_title_p1() -> None:
    check_incorrect_task_one_error(
        P1TaskModel, incorrect_task_with_too_long_title, "The title must be between 1 and 30 characters in length."
    )


def test_incorrect_task_with_too_long_title_p2() -> None:
    check_incorrect_task_one_error(
        P2TaskModel, incorrect_task_with_too_long_title, "The title must be between 1 and 30 characters in length."
    )


def test_incorrect_task_with_too_long_title_p3() -> None:
    check_incorrect_task_one_error(
        P3TaskModel, incorrect_task_with_too_long_title, "ensure this value has at most 30 characters"
    )


def test_incorrect_task_with_malformatted_title_p1() -> None:
    check_incorrect_task_one_error(
        P1TaskModel, incorrect_task_with_malformatted_title,
        "The title must be composed only of alphanumeric characters and spaces."
    )


def test_incorrect_task_with_malformatted_title_p2() -> None:
    check_incorrect_task_one_error(
        P2TaskModel, incorrect_task_with_malformatted_title,
        "The title must be composed only of alphanumeric characters and spaces."
    )


def test_incorrect_task_with_malformatted_title_p3() -> None:
    check_incorrect_task_one_error(
        P3TaskModel, incorrect_task_with_malformatted_title,
        "string does not match regex \"^[a-zA-Z0-9 ]+$\""
    )


# No such typed test exists for p1 as strict typing is not introduced


def test_incorrect_task_with_incorrectly_typed_title_p2() -> None:
    check_incorrect_task_one_error(P2TaskModel, incorrect_task_with_incorrectly_typed_title, "str type expected")


def test_incorrect_task_with_incorrectly_typed_title_p3() -> None:
    check_incorrect_task_one_error(P3TaskModel, incorrect_task_with_incorrectly_typed_title, "str type expected")


def test_incorrect_task_with_too_long_description_p1() -> None:
    check_incorrect_task_one_error(
        P1TaskModel, incorrect_task_with_too_long_description, "The description must be at most 200 characters."
    )


def test_incorrect_task_with_too_long_description_p2() -> None:
    check_incorrect_task_one_error(
        P2TaskModel, incorrect_task_with_too_long_description, "The description must be at most 200 characters."
    )


def test_incorrect_task_with_too_long_description_p3() -> None:
    check_incorrect_task_one_error(
        P3TaskModel, incorrect_task_with_too_long_description, "ensure this value has at most 200 characters"
    )


# No such typed test exists for p1 as strict typing is not introduced

def test_incorrect_task_with_incorrectly_typed_description_p2() -> None:
    check_incorrect_task_one_error(P2TaskModel, incorrect_task_with_incorrectly_typed_description, "str type expected")


def test_incorrect_task_with_incorrectly_typed_description_p3() -> None:
    check_incorrect_task_one_error(P3TaskModel, incorrect_task_with_incorrectly_typed_description, "str type expected")


def test_correct_task_with_valid_datetime_string_p1() -> None:
    task = P1TaskModel(**correct_task_with_valid_datetime_string)
    expected_dict = deepcopy(correct_task_with_valid_datetime_string)
    # noinspection PyTypedDict
    expected_dict["dueDatetime"] = datetime.fromisoformat(expected_dict["dueDatetime"])
    assert_model_dicts_equal(task.dict(by_alias = True), expected_dict)


def test_correct_task_with_valid_datetime_string_p2() -> None:
    task = P2TaskModel(**correct_task_with_valid_datetime_string)
    expected_dict = deepcopy(correct_task_with_valid_datetime_string)
    # noinspection PyTypedDict
    expected_dict["dueDatetime"] = datetime.fromisoformat(expected_dict["dueDatetime"])
    convert_to_p2_expected_dict(expected_dict)
    assert_model_dicts_equal(task.dict(by_alias = True), expected_dict)


def test_correct_task_with_valid_datetime_string_p3() -> None:
    task = P3TaskModel(**correct_task_with_valid_datetime_string)
    expected_dict = deepcopy(correct_task_with_valid_datetime_string)
    # noinspection PyTypedDict
    expected_dict["dueDatetime"] = datetime.fromisoformat(expected_dict["dueDatetime"])
    convert_to_p3_expected_dict(expected_dict)
    assert_model_dicts_equal(task.dict(by_alias = True), expected_dict)


def test_incorrect_task_with_unsupported_datetime_string_p1() -> None:
    check_incorrect_task_one_error(
        P1TaskModel, incorrect_task_with_unsupported_datetime_string, "invalid datetime format"
    )


def test_incorrect_task_with_unsupported_datetime_string_p2() -> None:
    check_incorrect_task_one_error(
        P2TaskModel, incorrect_task_with_unsupported_datetime_string, "invalid datetime format"
    )


def test_incorrect_task_with_unsupported_datetime_string_p3() -> None:
    check_incorrect_task_one_error(
        P3TaskModel, incorrect_task_with_unsupported_datetime_string, "invalid datetime format"
    )
