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


if __name__ == '__main__':
    print(foo())
