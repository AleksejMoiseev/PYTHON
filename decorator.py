from functools import wraps
from datetime import date


def boo(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("I am decorations func")
        result = func(*args, **kwargs)
        print('!!!!', date.today())
        return result
    return inner


@boo
def foo():
    return "FOO"
    with open("ttt.txt", 'w') as file:
        a = file.read()

    print(a)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b





if __name__ == '__main__':
    import itertools

    #print(list(itertools.islice(fib(), 100)))
    for i in fib(100):
        print(i)
