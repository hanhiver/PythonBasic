#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:51:23 2019

@author: dhan
"""

import numpy as np

def spec_histogram(input_list):
    hist, edges = np.histogram(input_list)
    hist = hist * 50 // hist.max()
    for (h, e) in zip(hist, edges):
        print(e, ": ", "*"*h)

a = [ [0, 0, 0, 0, 0, 0], 
      [0, 0, 1, 0, 0, 0], 
      [0, 1, 0, 1, 1, 0], 
      [1, 0, 0, 0, 0, 1], 
      [0, 0, 0, 0, 0, 0]]


a = np.array(a, dtype=np.uint8)
print(a)
print()

b = a.argsort(axis=0)
print(b)
print()

c = b[-1] - b[-1].min()
print(c)
print()

d = c*254//c.max()
print(d)
print()

e = np.vstack([a, d])
print(e)
print()

e = e[::-1]
print(e)
print()

m = np.random.laplace(loc=15, scale=3, size=500)
spec_histogram(m)

