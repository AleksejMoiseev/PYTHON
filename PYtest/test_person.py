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



class Ship:
    def __init__(self, coordinates, hit_coordinates):
        self.coordinates = coordinates
        self.hit_coordinates = hit_coordinates

    def to_json(self):
        return {'coordinates': self.coordinates, 'hit_coordinates': self.hit_coordinates}

    def __str__(self):
        return f"'coordinates': {self.coordinates}, 'hit_coordinates': {self.hit_coordinates}"

    def check_hit(self, coordinate):
        if not (coordinate in self.coordinates):
            return 'mimo'
        if not (coordinate in self.hit_coordinates):
            self.hit_coordinates.append(coordinate)
        if len(self.coordinates) == len(self.hit_coordinates):
            return 'killed'
        return 'ranen'

    def killed(self):
        if len(self.coordinates) == len(self.hit_coordinates):
            return True
        return False

@pytest.fixture
def ship_1():
    ship = Ship(coordinates=[], hit_coordinates=['A1'])
    return ship


@pytest.fixture
def ship_2():
    ship = Ship(coordinates=['A1', 'H7'], hit_coordinates=['A1'])
    print(ship.coordinates)
    return ship


@pytest.fixture
def ship_3():
    ship = Ship(coordinates=['A1', 'H7', "k5"], hit_coordinates=['A1'])
    return ship


def test_killed(ship_2):
    print(ship_2.coordinates)
    assert True
