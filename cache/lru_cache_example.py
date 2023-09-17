from datetime import timedelta, datetime
from functools import lru_cache, wraps
from time import sleep


@lru_cache(maxsize=64)
def get_items(key):
    '''Здесь бурная деятельность'''
    return 2


def timed_lru_cache(seconds, maxsize: int = 128):
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                print('!!!!!!!!!!!!!!!!!!!!!!!!')
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache


@timed_lru_cache(seconds=1)
def get_item_2(key):
    return 2

class A:
    def get_item_2(key):
        return 2



if __name__ == '__main__':
    key = 'qqq'
    # print(get_items(key))
    # print(get_items(key))
    # print(get_items(key))
    # print(get_items(key))
    # print(get_items(key))
    # print(get_items(key))
    # print(get_items.cache_info())
    #
    # print(get_item_2(key))
    # print(get_item_2(key))
    # sleep(1)
    # print(get_item_2(key))
    # print(get_item_2(key))
    # print(get_item_2(key))


