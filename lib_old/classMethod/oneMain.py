import types


class A(object):
	#age = 0

	def __init__(self, name):
		self.name = name
		self.age = len(name)

	def printName(self):
		print("A.printName(): my name is: {}".format(self.name))

"""
@classmethod
def printAge(cls):
	print("A.printAge(): my age is: {}".format(cls.age))
"""
def printAge(self):
	 print("A.printAge(): my age is: {}".format(self.age))
	 self.printName()

#A.printAge = printAge

a = A("Original")
a.printName()

a.printAge = types.MethodType(printAge, a)

a.printAge()

