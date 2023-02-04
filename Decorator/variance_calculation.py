import time
from functools import wraps


class average_time_function:

    def __init__(self, debug, average_time: float = 10):
        self.debug = debug
        self.average_time = average_time
        self.storage = []
        self.monotonic = time.monotonic()

    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            if not self.debug:
                return func(*args, **kwargs)
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.storage.append(round(end_time - start_time, 3))
            if time.monotonic() - self.monotonic >= self.average_time:
                self.monotonic = time.monotonic()
                print(f"The average time of one operation `{func.__name__}` function"
                      f"  per period {self.average_time} sec."
                      f" is equal to: {round(sum(self.storage)/len(self.storage), 2)} sec")
                self.storage = []
            return result

        return inner


@average_time_function(debug=True, average_time=0.01)
def foo():
    """ Это docstring"""
    #time.sleep(random.randint(1, 5))
    pass

if __name__ == '__main__':
    for i in range(0, 100000):
        foo()