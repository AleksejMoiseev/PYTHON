from datetime import date
from person.person import Person
import pytest


# class NameTooLong(Exception):
#     pass
#
#
# class person:
#     _CONST_LITERAL_NAME = 50
#
#     def __init__(self, name, birth_day):
#         self.name = name
#         self._birth_day = birth_day
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, val):
#         self.check_name(val)
#         self._name = val
#
#     @property
#     def birth_day(self):
#         return self._birth_day
#
#     @birth_day.setter
#     def birth_day(self, val):
#         self._birth_day = val
#
#     @property
#     def age(self):
#         date_now = datetime.date.today()  # Поиск текущей даты
#         data = (date_now - self.birth_day)  # Получаем количество дней как разность
#         return data.days//365
#
#     @staticmethod
#     def check_name(name):
#         if len(name) > person._CONST_LITERAL_NAME:
#             raise NameTooLong()
#

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


