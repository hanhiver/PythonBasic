import multiprocessing as mp
import numpy as np
import ctypes

def func(array):
    print("I got: ", array)

def main():
    lock = mp.Lock()

    a = np.array(range(5))

    p = mp.Process(target = func, args = (a, ))
    
    p.start()
    p.join()

if __name__ == '__main__':
    main()
