import os
import multiprocessing 
from time import sleep 

def run():
    while True:
        print('RUN pid: ', os.getpid())
        sleep(1)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target = run)
    p2 = multiprocessing.Process(target = run)

    p1.start()
    print('P1 started.')
    p2.start()
    print('P2 started.')

    p1.join()
    p2.join()



