import time, random
from multiprocessing import Process, Pipe, current_process
from multiprocessing.connection import wait
from time import time, sleep

def foo(w):
    for i in range(5):
        sleep(1)
        w.send((i, current_process().name))
    w.close()

if __name__ == '__main__':
    start = time()

    readers = []

    for i in range(2):
        r, w = Pipe(duplex=False)
        readers.append(r)
        p = Process(target = foo, args = (w,))
        p.start()
        w.close()

    while readers:
        for r in wait(readers):
            try:
                msg = r.recv()
            except EOFError:
                readers.remove(r)
            else:
                print(msg)
    
    print('Finished in ', time() - start)

