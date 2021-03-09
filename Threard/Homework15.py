#!/usr/bin/env python3
""""
Run callables with list of arguments in parallelograms.If there was an exception in one of the
threadsit should be raised in the main thread whenignore_exceptions=True
"""
from concurrent.futures import ThreadPoolExecutor


class MyException(Exception):
    pass


class ParallelObject:

    def __init__(self, items, timeout=10, ignore_exceptions=True):
        super().__init__()
        self.items = items
        self.timeout = timeout
        self.ignore_exceptions = ignore_exceptions

    def _run_exceptions(self, fn):
        results = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            for item in self.items:
                future = executor.submit(fn, item)
                results.append(future)
            for result in results:
                try:
                    print(result.result(timeout=self.timeout))
                except MyException:
                    print(f"Exception {executor}")
            return results

    def _run_ignore_exceptions(self, fn):
        with ThreadPoolExecutor(max_workers=10) as executor:
            future = executor.map(fn, self.items, timeout=self.timeout)
        print(list(future))

    def run(self, fn):
        if self.ignore_exceptions:
            self._run_exceptions(fn)
        else:
            self._run_ignore_exceptions(fn)


def power_of_two(x):
    if x == 3:
        raise MyException
    return x ** 2


if __name__ == '__main__':
    ParallelObject(items=[1, 2, 3, 3, 4, 5, 6], ignore_exceptions=True).run(power_of_two)
