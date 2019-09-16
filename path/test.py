import sys
import os

if __name__ == '__main__':
    print("file:      ", __file__)
    print("abspath:   ", os.path.abspath(__file__))
    print("dirname:   ", os.path.dirname(os.path.abspath(__file__)))
    print("new path:  ", os.path.join(os.path.dirname(os.path.abspath(__file__))))

