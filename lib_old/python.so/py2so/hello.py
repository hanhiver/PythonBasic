import sys

def hello():
    print('In hello: ', *sys.argv)
    print('hello! Python so.')

def myname(name):
    print('In myname: ', *sys.argv)
    print('My name is: {}.'.format(name))

if __name__ == '__main__':
    print('In file: ', *sys.argv)
    hello()
    myname('dhan')

