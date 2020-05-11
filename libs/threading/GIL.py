import multiprocessing
import threading
import time

def task():
    i = 0
    for _ in range(10000000):
        i = i + 1
    return True

def single():
    start = time.time()

    threads_list = []

    for i in range(2):
        t = threading.Thread(target = task)
        threads_list.append(t)
        t.start()
        t.join()

    #for t in threads_list:
    #    t.join

    print('Single-thread finished in {} seconds.'.format(time.time() - start))

def multiple():
    start = time.time()

    threads_list = []

    for i in range(2):
        t = threading.Thread(target = task)
        threads_list.append(t)
        t.start()

    for t in threads_list:
        t.join()

    print('Multi-threads finished in {} seconds.'.format(time.time() - start))

def multipleP():
    start = time.time()

    process_list = []

    for i in range(2):
        p = multiprocessing.Process(target = task)
        process_list.append(p)
        p.start()

    for p in process_list:
        p.join()

    print('Multi-processes finished in {} seconds.'.format(time.time() - start))

def main():
    single()
    multiple()
    multipleP()

if __name__ == '__main__':
    main()




