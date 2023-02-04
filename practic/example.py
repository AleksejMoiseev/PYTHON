from time import sleep


class foo:
    def pprint(self):
        print('000000000')

class foo1(foo):
    def pprint(self):
        super().pprint()
        print('111111111')


class foo2(foo1):
    def pprint(self):
        super().pprint()
        print('22222222222')


class foo3(foo2):
    def pprint(self):
        super().pprint()
        print('333333333333')


class foo4(foo3, foo1):
    def pprint(self):
        super().pprint()
        print('44444444444444444')

from contextlib import contextmanager


@contextmanager
def foo():
    f = open('2.txt', 'r+')
    yield f
    f.close()


class Boo:

    def __enter__(self):
        self.f = open('2.txt', 'r+')
        return self.f

    def __exit__(self, exp1, exp2, ttt):
        self.f.close()


def cached_decorator(func):
    cach = {}

    def inner(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cach:
            result = cach[key]
            print('111111111')
        else:
            result = func(*args, **kwargs)
            cach[key] = result
            print('22222222')
        return result
    return inner


@cached_decorator
def foo(a):
    return a**2


def fibb():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

class ATest:
    def Atest(self):
        print('test')

class ATest1(ATest):
    def Atest(self):
        super().Atest()
        print('test1')

class ATest2(ATest):
    def Atest(self):
        super().Atest()
        print('test2')

class ATest3(ATest):
    def Atest(self):
        super().Atest()
        print('test3')

class RunMe(ATest1, ATest2, ATest3):
    def Atest(self):
        super().Atest()
        print('RunMe')



print('RunMe')

if __name__ == '__main__':
    # with foo() as CM:
    #     d = CM.read()
    # print(d)
    #
    # with Boo() as CM:
    #     d = CM.read()
    # print('@@@@', d)

    # for i in fibb():
    #     sleep(1)
    #     print(i)

    test = RunMe()
    test.Atest()
