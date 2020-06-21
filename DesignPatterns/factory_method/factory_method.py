'''
Factory Method
工厂方法模式是简单工厂模式的衍生，解决了许多简单工厂模式的问题。 
首先实现了‘开-闭’原则，实现了可扩展。 其次，更加复杂的层次结构可以应用于产品结果复杂的场合。 
工厂方法模式对简单工厂模式进行了抽象。有一个抽象的Factory类（可以是抽象类和接口），
这个类将这个类将不在负责具体的产品生产，而是只制定一些规范，
具体的生产工作由其子类去完成。在这个模式中，工厂类和产品类往往可以依次对应。
即一个抽象工厂对应一个抽象产品，一个具体工厂对应一个具体产品，
这个具体的工厂就负责生产对应的产品。
工厂方法模式(Factory Method pattern)是最典型的模板方法模式(Templete Method pattern)应用。
'''

class ShapeFactory(object):
    '''Factory class'''
    def getShape(self):
        return self.name

class Circle(ShapeFactory):
    def __init__(self):
        self.name = 'Circle'
    def draw(self):
        print('Circle')

class Rectangle(ShapeFactory):
    def __init__(self):
        self.name = 'Rectangle'
    def draw(self):
        print('Rectangle')

class ShapeInterfaceFactory(object):
    '''Interface base class'''
    def create(self):
        raise NotImplementedError

class ShapeCircle(ShapeInterfaceFactory):
    def create(self):
        return Circle()

class ShapeRectangle(ShapeInterfaceFactory):
    def create(self):
        return Rectangle()

if __name__ == "__main__":
    shape_interface1 = ShapeCircle()
    obj1 = shape_interface1.create() 
    obj1.getShape()
    obj1.draw()

    shape_interface2 = ShapeRectangle()
    obj2 = shape_interface2.create() 
    obj2.getShape()
    obj2.draw()
