# Meta class allow us to control a seris of class definition. 
# It can help us to avoid inaccurate class inherit from the definition part. 

print('Before Meta')
class Meta(type):
	print('In Meta')
	def __new__(meta, name, bases, class_dict):
		print(meta)
		print(name)
		print(bases)
		print(class_dict)
		return type.__new__(meta, name, bases, class_dict)
	print('After __new__')

print('Before MyClass')
class MyClass(object, metaclass = Meta):
	print('In MyClass')
	stuff = 123
	print('After stuff')

	print('Before foo')
	def foo(self):
		pass
	print('After foo')

class ValidatePolygon(type):
	def __new__(meta, name, bases, class_dict):
		if bases != (object,):
			if class_dict['sides'] < 3:
				raise ValueError('Polygon needs 3+ sides.')
		return type.__new__(meta, name, bases, class_dict)

class Polygon(object, metaclass = ValidatePolygon):
	sides = None 

	@classmethod
	def interior_angles(cls):
		return (cls.sides - 2) * 180

class Triangle(Polygon):
	sides = 3

'''
print('Before class')
class Line(Polygon):
	print('Before sides')
	sides = 1 
	print('After sides')
'''

