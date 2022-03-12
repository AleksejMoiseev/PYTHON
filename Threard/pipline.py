import os
from concurrent.futures.thread import ThreadPoolExecutor
from queue import Queue
import threading
import time


def __current_thread_name():
    return threading.current_thread()


def job1(q_in: Queue, q_out: Queue):
    value = q_in.get()
    print(__current_thread_name(), value)
    time.sleep(1)
    q_out.put(value ** 2)
    return q_out


def job2(q_in: Queue, q_out: Queue):
    value = q_in.get()
    print(__current_thread_name(), value)
    q_out.put(value + 100)
    return q_out


def job3(q_in: Queue, q_out: Queue):
    value = q_in.get()
    print(__current_thread_name(), value)
    q_out.put("Alex" + str(value))
    return q_out


def job4(q_in: Queue, q_out: Queue):
    value = q_in.get()
    print(__current_thread_name(), value)
    value_upper = value.upper()
    q_out.put(value_upper)
    return value_upper


jobs = [job1, job2, job3, job4]

COUNT_CPU = os.cpu_count() - 1
print('COUNT_CPU', COUNT_CPU)

first_value_for_my_job1 = Queue()
first_value_for_my_job1.put(5)


def pipeline():
    with ThreadPoolExecutor(max_workers=COUNT_CPU) as executor:
        q_in = first_value_for_my_job1
        for job in jobs:
            q_out = Queue()
            executor.submit(job, q_in=q_in, q_out=q_out)
            q_in = q_out
    return q_in.get()


if __name__ == '__main__':
    print(pipeline())

