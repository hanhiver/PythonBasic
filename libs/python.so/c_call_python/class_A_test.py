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

if __name__ == '__main__':
    a = A()
    a.run("abc")
    a.run2("def")
