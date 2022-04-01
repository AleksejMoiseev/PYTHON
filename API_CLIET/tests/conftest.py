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


ACCESS_TOKEN = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwayI6MH0.99Q7zHnAZVqblwg93gjXYRCB-LmOuhfWjWWqx0ei5fg"
REFRESH_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9" \
                ".eyJleHAiOjE2NDc1ODcxNzJ9.H2gTn-_QYxegb8lO7yHFpk-ntZN7hp0X5jDt6fU0izk"


@pytest.fixture
def login_password():
    return "login", "password"


@pytest.fixture
def email():
    return "alex@mail.ru"


@pytest.fixture
def headers_auth():
    headers = {'Authorization': ACCESS_TOKEN}
    return headers



