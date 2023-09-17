from functools import wraps, reduce
from itertools import chain


cache = {}


def get_items(key):
    if key in cache:
        return cache[key]
    print('!!!!')
    value = 2  # Очень тяжелый запрос в базу данных для получения данных справочника и трудоемкое математическое
    # вычисление
    cache[key] = value
    return value


class cached:

    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            key = self._build_key(*args, **kwargs)
            if key in self.cache:
                return self.cache[key]
            print("Make difficult calculator", key)
            result = func(*args, **kwargs)
            self.cache[key] = result
            return result

        return inner

    @staticmethod
    def _build_key(*args, **kwargs):
        value = chain(*args, kwargs.values())
        return reduce(lambda x, y: x + y, value)


@cached()
def get_item_2(key):
    """Очень сложные вычисления"""
    return 2

if __name__ == '__main__':
    key = 'aaa'
    # print(get_items(key))
    # print(get_items(key))
    # print(get_items(key))
    # print(get_items(key))
    # print(get_items(key))

    print(get_item_2(key=key))
    print(get_item_2(key=key))
    print(get_item_2(key=key))
    print(get_item_2(key=key))
    print(get_item_2(key=key))
    print(get_item_2(key=key))

