#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:45:01 2019

@author: dhan
"""

import gc 
import sys 

class CGcleak(object):
    def __init__(self):
        self._text = '#' * 10
        
    def __del__(self):
        pass
    
def make_cycle_ref():
    _gcleak = CGcleak()
    print("_gcleak ref count0: {}".format(sys.getrefcount(_gcleak)))
    del _gcleak
    try:
        print('_gcleak ref count1: {}'.format(sys.getrefcount(_gcleak)))
    except UnboundLocalError:
        print('_gcleak is invalid!')
        
def test_gcleak():
    gc.enable()
    #gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_LEAK)
    
    print('begin leak test...')
    make_cycle_ref()
    
    print('\nbegin collect...')
    _unreachable = gc.collect()
    
    print('unreachable object num: {}'.format(_unreachable))
    print('garbage object num: {}'.format(len(gc.garbage)))
    
if __name__ == '__main__':
    test_gcleak()
    