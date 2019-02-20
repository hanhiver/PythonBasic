import threading
import time

def task():
    i = 0
    for _ in range(10000000):
        i = i + 1
    return True

def main():
    start = time.time()

    threads_list = []

    for i in range(2):
        t = threading.Thread(target = task)
        threads_list.append(t)
        t.start()
        t.join()

    #for t in threads_list:
    #    t.join

    print('Program finished in {} seconds.'.format(time.time() - start))

if __name__ == '__main__':
    main()






