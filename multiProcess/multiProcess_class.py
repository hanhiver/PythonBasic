import multiprocessing
import time
import sched
import queue
import os

mystr = 'aaa'

class Test():
    def __init__(self):
        self.queue = multiprocessing.Queue()
        self.scheduler = sched.scheduler()
        self.sub_process = multiprocessing.Process(target = self.my_process)
        self.sub_process.start()

    def func(self):
        print('my func in.')
        self.scheduler.enter(1, 1, self.func)
        time.sleep(1)
        print('my func out.')

    def my_process(self):
        self.scheduler.enter(1, 1, self.func) 
        self.scheduler.run()

    def __del__(self):
        self.sub_process.join()

class SchedRun():
    def __init__(self, func, args, init_func = None, init_args = {}, interval = 0.04, init_interval = 0.5):
        self.func = func
        self.args = args
        self.init_func = init_func
        self.init_args = init_args
        self.interval = interval
        self.init_interval = init_interval

        self.scheduler = sched.scheduler()
        self.sub_process = multiprocessing.Process(target = self.wrap_process)
        self.sub_process_continue = True
        self.sub_process.start()

    def __del__(self):
        self.sub_process.join()

    def wrap_func(self):
        if self.sub_process_continue:
            self.scheduler.enter(self.interval, 1, self.wrap_func)
            self.sub_process_continue = self.func(self.args)
        else:
            return

    def wrap_process(self):
        if self.init_func:
            self.init_func(*self.init_args)

        self.scheduler.enter(self.init_interval, 1, self.wrap_func) 
        self.scheduler.run()

def myinit():
    global mystr 

    mystr = 'bbb'

    print('Init func. ', os.getpid(), mystr)

def myfunc(input_queue, timeout = 3):
    global mystr 

    try:
        value = input_queue.get(timeout = timeout)
        print('Doing my job: ', value, os.getpid(), mystr)
        return True
    except queue.Empty:
        print('Queue empty.')
        return False


def main():
    global mystr

    print('Main process: ', os.getpid(), mystr)
    my_queue = multiprocessing.Queue()
    test = SchedRun(myfunc, my_queue, init_func = myinit, interval = 1)

    for i in range(10):
        my_queue.put(i)

    time.sleep(3)
    print('Main process END: ', os.getpid(), mystr)
    
if __name__ == '__main__':
    main()


