"""
Имплементация декоратора с аргументами через класс
"""
import time
import random
from functools import wraps


class measure_time:

    def __init__(self, debug):
        self.debug = debug

    def __call__(self, my_func):
        @wraps(my_func)
        def inner(*args, **kwargs):
            start_time = time.time()
            if self.debug:  # Используем аргумент декоратора
                print(f"Функция начала свой бег: {start_time}")
            result_my_func = my_func(*args, **kwargs)
            end_time = time.time()
            if self.debug:
                print(f"Функция закончила бежать: {end_time}")
            print(f" Итого бежала: {end_time - start_time}")
            return result_my_func

        return inner


@measure_time(debug=False)
def foo():
    """ Это docstring"""
    print("Start to run")
    time.sleep(random.randint(1, 5))
    print("Stop running...")


if __name__ == '__main__':
    foo()
