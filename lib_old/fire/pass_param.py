#!/usr/bin/env python
import fire

class caculator(object):
    
    def __init__(self, offset=0):
        self._offset = offset

    def add(self, x, y):
        return x + y + self._offset
    
    def mul(self, x, y):
        return x * y + self._offset

def main():
    fire.Fire(caculator)
    
if __name__ == '__main__':
    main()
    