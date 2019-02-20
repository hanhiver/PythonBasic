import main_args
from main_args import *
import sys

if __name__ == '__main__':
    print('In file: ', *sys.argv)
    main_args.main()

