from check_person.person_for_check import Person
import pytest
from datetime import date

"""
fixture - function make прекондишен for test 
"""


@pytest.fixture
def fixture_for_test():
    person = Person(name="Fedor", birth_day=date(year=1979, month=10, day=3))
    return person

"""
@pytest.mark.parametrize позволяет проводить тесты с несколькими аргументами
"""


@pytest.mark.skip("Здесь пишется комментарий причина почему тест заскипили")  # Позволяет заскипить тесты до устранения бага тесты не участвуют в проверке
@pytest.mark.parametrize("value", ["fedor", "Fedor"])  # в кавычках указываем аргументы через запятую в кавычках
# который хотим передать и передаем его как аргумент в функцию, далее список tuples или значений исходя из количества
# аргументов
def test_proba_name(fixture_for_test, value):  # Используем fixture: fixture_for_test as return person
    # и value из pytest.mark.parametrize
    assert fixture_for_test.name == value


"""
Для запуска тестов в консоле запускаем команду :
 pytest -v test_person_for_check.py # где -v verbose выводит данные с наполненной информацией
или
 pytest test_person_for_check.py
"""

"""
Pytest как умный runner способен также запускать формат unit test
"""


@pytest.mark.my_metka
def test_mark():
    assert 1 == 1

"""
можно запускать тесты помеченные меткой как выше на примере помечено меткой  string == my_metka

запуск: $ pytest -m my_metka test_person_for_check.py

"""