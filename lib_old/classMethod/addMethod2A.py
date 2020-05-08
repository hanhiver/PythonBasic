import types

import classA

"""
@classmethod
def printAge(cls):
	print("A.printAge(): my age is: {}".format(20))

classA.A.printAge = printAge
"""

def printAge(self, input):
	print("A.printAge(): my age is: {} and input is {}".format(self.age, input))

def getA(**kwargs):
	a = classA.A(**kwargs)
	a.printAge = types.MethodType(printAge, a)
	return a
