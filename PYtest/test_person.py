from datetime import date
from person.person import Person
import pytest


@pytest.fixture
def empty_person():
    expected_name = "Fedor"
    expected_date = date(year=1979, month=8, day=3)
    fedor = Person(name=expected_name, birth_day=expected_date)
    return fedor


def test_basic(empty_person):
    print(empty_person.name)
    print(empty_person.age)
    assert empty_person.name == "Fedor"


