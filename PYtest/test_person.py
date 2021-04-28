from datetime import date
from person.person import Person
import pytest


@pytest.fixture
def empty_person():
    expected_name = "Fedor"
    expected_date = date(year=1979, month=8, day=3)
    fedor = Person(name=expected_name, birth_day=expected_date)
    return fedor


@pytest.fixture
def old_person():
    expected_name = "Alex"
    expected_date = date(year=1994, month=6, day=6)
    fedor = Person(name=expected_name, birth_day=expected_date)
    return fedor


@pytest.mark.newbasic  # Метка для запуска набираем pytest -v -m new_basic
def test_basic(empty_person):
    print(empty_person.name)
    print(empty_person.age)
    assert empty_person.name == "Fedor"


# Пример работы с марк
@pytest.mark.parametrize("age,name_p", [(41, "Fedor"), (41, "Fedor")])
def test_two_basic(old_person, age, name_p):
    assert old_person.name != name_p
    assert old_person.age != age


@pytest.mark.newbasic  # Метка для запуска набираем pytest -v -m new_basic
def test_check_zerodivisions():
    with pytest.raises(expected_exception=ZeroDivisionError):  # отлавливает Exceptions
        a = 5 / 0
        print(a)
