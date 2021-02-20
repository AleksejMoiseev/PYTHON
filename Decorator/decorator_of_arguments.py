"""
Декоратор с аргументами
"""
import time
import random
from functools import wraps


def measure_time(debug):  # в случае декоратора с аргументами сначала запускаем функцию содержащую аргументы
    def _measure_time(my_func):  # далее пишем обычный декоратор в котором используем аргументы из внешней функции
        # для имплементации логики
        @wraps(my_func)
        def inner(*args, **kwargs):
            start_time = time.time()
            if debug:  # Используем аргумент декоратора
                print(f"Функция начала свой бег: {start_time}")
            result_my_func = my_func(*args, **kwargs)
            end_time = time.time()
            if debug:
                print(f"Функция закончила бежать: {end_time}")
            print(f" Итого бежала: {end_time - start_time}")
            return result_my_func
        return inner
    return _measure_time


@measure_time(debug=True)
def foo():
    """ Это docstring"""
    print("Start to run")
    time.sleep(random.randint(1, 5))
    print("Stop running...")


if __name__ == '__main__':
    foo()

