#!/usr/bin/env python
import fire

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

def hello(name=None):
    if name is not None:
        print("Hello! ", name)
    else:
        print("Please input name.")
        exit(-1)

if __name__ == '__main__':
    fire.Fire({
        'add': add, 
        'mul': mul, 
        'hello': hello, 
    })
