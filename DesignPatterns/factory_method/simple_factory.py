"""
Simple Factory Method
"""

class Shape(object):
    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def draw(self):
        print('draw circle')

class Rectangle(Shape):
    def draw(self):
        print('draw rectangle')

class ShapeFactory(object):
    def create(self, shape):
        if shape == 'Circle':
            return Circle()
        elif shape == 'Rectangle':
            return Rectangle()
        else:
            return None

factory = ShapeFactory()
obj1 = factory.create('Circle')
obj1.draw()
obj2 = factory.create('Rectangle')
obj2.draw()

