#!/usr/bin/env python3
"""
1.Имплементировать декоратор:@retry(n=5, interval=1.5 с,
allowed_exceptions=(Exception, ),verbose=True)
декорируемая функция get_product():
"""

from functools import wraps
import time
from HW12.product_for_retry import Product, NothingToRetrieveException, retrieve_product


class ProductNotFoundException(NothingToRetrieveException):
    pass


class retry:
    ALLOWED_EXCEPTIONS = (NothingToRetrieveException, ProductNotFoundException)

    def __init__(self, n, interval, verbose, allowed_exceptions=ALLOWED_EXCEPTIONS):
        self.n = n
        self.interval = interval
        self.verbose = verbose
        self.allowed_exceptions = allowed_exceptions

    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            val = None
            retry_number = 0
            for i in range(0, self.n):
                retry_number += 1
                if self.verbose:
                    print(f"Retrying <{func.__name__}>. Try #{retry_number}  ")
                try:
                    val = func(*args, **kwargs)
                except self.allowed_exceptions:
                    print("Внимание повторяю запрос")
                else:
                    break
                time.sleep(self.interval)
            return val

        return inner


@retry(n=5, interval=1.5, verbose=True)
def get_product():
    try:
        get_product_dict = retrieve_product()
    except NothingToRetrieveException:
        raise ProductNotFoundException()
    else:
        format_for_serialization = get_product_dict['format']
        data_for_serialization = get_product_dict['serialized_str']
        print(format_for_serialization)
        return Product.choice_from_serialization(str_format=format_for_serialization,
                                                 str_for_serialization=data_for_serialization)


if __name__ == '__main__':
    print(get_product())
