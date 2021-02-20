"""
Имплементация Сингелтон самостоятельно
"""


class NewClassSingeleton(object):  # Лучше обозначить в названии, что это Singeleton
    _instance = None

    def __init__(self, name):
        print("start constractor")
        self.name = name

    def __new__(cls, *args, **kwargs):
        print("start new")
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance


if __name__ == '__main__':
    s1 = NewClassSingeleton("name1")
    print(s1.name)
    s2 = NewClassSingeleton("name2")
    print(s1.name)
    print(s1, s2)
