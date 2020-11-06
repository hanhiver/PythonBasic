class A:
    def __init__(self):
        self.x="xueluo" 

    def run(self,y):
        print('y:{}'.format(y))
        _x = self.x
        print('_x:{}'.format(_x))
        return y

    def run2(self,y):
        print('y:{}'.format(y))
        return "xueluo" +y

def say_hello(a):
    a = a+a
    print(a)

def say_hello1():
    print("Hello, i came from python. ")

def main():
    a = A()
    a.run("abc")
    a.run2("def")

def run2_wrapper(x):
    a = A()
    print("Execute run2 with arg: ", x)
    return a.run(x)
    

if __name__ == '__main__':
    main()