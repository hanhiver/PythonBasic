#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:42:14 2019

Testing program that share the numpy array between different processes. 

@author: dhan
"""

import multiprocessing as mp
from multiprocessing.sharedctypes import RawArray
#from multiprocessing.sharedctypes import copy
import ctypes
import numpy as np

def func(array):
    print(type(array))
    for i in range(3):
        print("Child: ", array[i])
    
    temp_array = np.array(array, dtype = np.ubyte)
    temp_array += 3
    #temp_array = np.array(range(2, -1, -1), dtype = np.ubyte)
    print(ctypes.sizeof(array))
    print(np.ctypeslib.as_ctypes(temp_array))
    # 子进程通过这样的方式将ndarray中的内容拷贝到共享内存中去。
    ctypes.memmove(array, np.ctypeslib.as_ctypes(temp_array), ctypes.sizeof(array))
    #for i in range(3):
    #    array[i] = temp_array[i]

def main():
    a = np.array(range(3))
    shared_array = RawArray(ctypes.c_ubyte, a)
    
    for i in range(3):
        print("Parent: ", shared_array[i])
    
    p = mp.Process(target = func, args = (shared_array, ))
    p.start()
    p.join()
    
    for i in range(3):
        print("After Parent: ", shared_array[i])
    
if __name__ == '__main__':
    main()
    
