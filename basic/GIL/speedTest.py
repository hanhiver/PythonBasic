import time
from functools import wraps
from threading import Thread

def run_time(fn):
    @wraps(fn)
    def print_run_time(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(fn.__name__ + " took " + str(end_time - start_time) + " seconds.")
        return result
    return print_run_time

def count(n):
    while n > 0:
        n -= 1

@run_time
def one_thread(n):
    count(n)

@run_time
def two_thread(n):
    t1 = Thread(target=count, args=(n/2,))
    t2 = Thread(target=count, args=(n/2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    count_number = 40000000
    one_thread(count_number)
    two_thread(count_number)


