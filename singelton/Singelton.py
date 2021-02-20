"""
Имплементация Singelton
"""

class Foo:
    _instance = None
    name = "Fedor"

    def __new__(cls, *argv, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    


if __name__ == '__main__':
    f = Foo()
    f1 = Foo()
    print(f1.name)
    print(f.name, f1)