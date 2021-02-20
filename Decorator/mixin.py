"""
Mixin - Класс не предназначен для порождения самостоятельных обьектов не создаем инстанс,
 используется для корректировки поведения других классов, у этого класса не может быть констрактора __init__
 есть только методы, от мы добавляем эти методы к какому то классу
 имплементируется  через наследования
"""
import json


class JsonSerilizaMixin:  # Создание
    def to_json(self):
        return json.dumps(self.__dict__)


class Person(JsonSerilizaMixin):

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        """

        :return: Возвращает стринговое представление обьекта
        """
        return f"name: {self.name}, last_name:{self.last_name}"


if __name__ == '__main__':
     p = Person(name="Alex", last_name="Moiseev")
     print(p.__dict__)  # возвращает dict состоящей и init констрактора
     print(p.to_json())