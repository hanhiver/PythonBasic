class A(object):
	def __init__(self, **kwargs):
		self.name = "Original"
		self.age = len(self.name)
		self.args = kwargs

	def printName(self):
		print("A.printName(): my name is: {}".format(self.name))

	def printArgs(self):
		print(self.args)

