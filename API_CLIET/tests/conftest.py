import pytest


@pytest.fixture
def expected_value_id_1():
    return [{'1': 'issue_Alex'}]


@pytest.fixture
def expected_value_for_create():
    return {"id": 1, "name": 'issue_Alex'}


@pytest.fixture
def limit():
    return 1


@pytest.fixture
def offset():
    return 1


@pytest.fixture
def expected_exception():
    return "Issues Not Found"

