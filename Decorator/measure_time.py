"""
Создать декаратор который поменяет выполнение функции след образом до
 и после будет печать время и  время которое бежала функция
 @measure_time
"""
import time
import random
from functools import wraps


def measure_time(my_func):  # декаратор представляет из себя функцию которая оборачивает другую функцию
    # и добавляет ей функциональность
    @wraps(my_func)  # позволяет сохранить все полезное при использовании декараторов, в частности сохранен docstring
    def inner(*args, **kwargs):  # Здесь пишется функциональность декоратора
        # inner.__doc__ = my_func.__doc__  # Это строка позволяет сохранить docstring
        start_time = time.time()
        print(f"Функция начала свой бег: {start_time}")
        result_my_func = my_func(*args, **kwargs)  # сохраняем в переменую результат оригинальной функции
        end_time = time.time()
        print(f"Функция закончила бежать: {end_time}")
        print(f" Итого бежала: {end_time - start_time}")
        return result_my_func  # возвращаем результат оригинальной функции
    return inner  # возвращаем обьект содержащий результат оригинальной функции


@measure_time
def foo():
    """ Это docstring"""  # при запуске докстринг не воспроизводится т.е print(foo.__doc__) будет равно None
    #  для сохранения докстринга дописываем в декоратор  inner.__doc__ = my_func.__doc__
    #  также можно воспользоваться встроенным в from functools import wraps декоратором @wraps(my_func)
    print("Start to run")
    time.sleep(random.randint(1, 5))
    print("Stop running...")


def cached(func):
    from functools import wraps
    cach = {}

    @wraps(func)
    def inner(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cach.keys():
            return cach[key]
        else:
            result = func(*args, **kwargs)
            cach[key] = result
            return result
    return inner


@cached
def boo(n):
    return n**2


if __name__ == '__main__':
    # foo()
    # print(foo.__doc__)  # печатает None
    print(boo(n=4))
    print(boo(n=4))
    print(boo(n=4))
    print(boo(n=4))
    print(boo(n=4))
