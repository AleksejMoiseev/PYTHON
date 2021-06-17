"""
Задача: создать класс person  и провести тестировaние через pytest
"""

import datetime
import os
from pathlib import Path


class NameTooLong(Exception):
    pass


class Person:
    _CONST_LITERAL_NAME = 50

    def __init__(self, name, birth_day):
        self.name = name
        self._birth_day = birth_day

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self.check_name(val)
        self._name = val

    @property
    def birth_day(self):
        return self._birth_day

    @birth_day.setter
    def birth_day(self, val):
        self._birth_day = val

    @property
    def age(self):
        date_now = datetime.date.today()  # Поиск текущей даты
        data = (date_now - self.birth_day)  # Получаем количество дней как разность
        return data.days//365

    @staticmethod
    def check_name(name):
        if len(name) > Person._CONST_LITERAL_NAME:
            raise NameTooLong()


if __name__ == '__main__':
    person = Person(name="fedor", birth_day=datetime.date(year=1979, month=10, day=3))
    # print(os.path.dirname(__file__))
    path = os.path.join(os.path.dirname(__file__), 'person_for_check.py')
    BASE_DIRs = Path(__file__).resolve().parent.parent.joinpath('check_person/person_for_check.py')

    print(BASE_DIRs)