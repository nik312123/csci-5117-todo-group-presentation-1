from datetime import datetime

from pydantic.color import Color

from p1_siyad_final import task_model as p1_task_model
from p2_sumukh_final import task_model as p2_task_model
from p3_aaron_final import task_model as p3_task_model

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


def convert_to_p3_expected_dict(expected_dict: dict) -> None:
    expected_dict["color"] = Color(expected_dict["color"])
    expected_dict["user"].pop("hasMiddleName")


def test_correct_task_with_no_middle_name_with_field_p1() -> None:
    task = p1_task_model.TaskModel(**correct_task_with_no_middle_name_with_field)
    assert_model_dicts_equal(task.dict(by_alias = True), correct_task_with_no_middle_name_with_field)


def test_correct_task_with_no_middle_name_with_field_p2() -> None:
    task = p2_task_model.TaskModel(**correct_task_with_no_middle_name_with_field)
    assert_model_dicts_equal(task.dict(by_alias = True), correct_task_with_no_middle_name_with_field)


def test_correct_task_with_no_middle_name_with_field_p3() -> None:
    task = p3_task_model.TaskModel(**correct_task_with_no_middle_name_with_field)
    expected_dict = correct_task_with_no_middle_name_with_field.copy()
    convert_to_p3_expected_dict(expected_dict)
    assert_model_dicts_equal(task.dict(by_alias = True), expected_dict)


def test_correct_task_with_no_middle_name_without_field_p1() -> None:
    task = p1_task_model.TaskModel(**correct_task_with_no_middle_name_without_field)
    expected_dict = correct_task_with_no_middle_name_without_field.copy()
    # noinspection PyTypeChecker
    expected_dict["user"]["middleName"] = None
    assert_model_dicts_equal(task.dict(by_alias = True), correct_task_with_no_middle_name_without_field)


def test_correct_task_with_no_middle_name_without_field_p2() -> None:
    task = p2_task_model.TaskModel(**correct_task_with_no_middle_name_without_field)
    expected_dict = correct_task_with_no_middle_name_without_field.copy()
    # noinspection PyTypeChecker
    expected_dict["user"]["middleName"] = None
    assert_model_dicts_equal(task.dict(by_alias = True), correct_task_with_no_middle_name_without_field)


def test_correct_task_with_no_middle_name_without_field_p3() -> None:
    task = p3_task_model.TaskModel(**correct_task_with_no_middle_name_without_field)
    expected_dict = correct_task_with_no_middle_name_without_field.copy()
    # noinspection PyTypeChecker
    expected_dict["user"]["middleName"] = None
    convert_to_p3_expected_dict(expected_dict)
    assert_model_dicts_equal(task.dict(by_alias = True), expected_dict)


def test_correct_task_with_middle_name_p1() -> None:
    task = p1_task_model.TaskModel(**correct_task_with_middle_name)
    assert_model_dicts_equal(task.dict(by_alias = True), correct_task_with_middle_name)


def test_correct_task_with_middle_name_p2() -> None:
    task = p2_task_model.TaskModel(**correct_task_with_middle_name)
    assert_model_dicts_equal(task.dict(by_alias = True), correct_task_with_middle_name)


def test_correct_task_with_middle_name_p3() -> None:
    task = p3_task_model.TaskModel(**correct_task_with_middle_name)
    expected_dict = correct_task_with_middle_name.copy()
    convert_to_p3_expected_dict(expected_dict)
    assert_model_dicts_equal(task.dict(by_alias = True), expected_dict)
