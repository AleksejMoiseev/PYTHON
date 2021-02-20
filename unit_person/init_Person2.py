
import datetime

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
    t = Person(name="Fedor", birth_day=datetime.date(year=1979, month=8, day=3))
    print(t.age)

