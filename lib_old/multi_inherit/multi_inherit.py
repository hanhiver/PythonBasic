class MyBaseClass:
	def __init__(self, value):
		self.value = value

class MyAddTwo(MyBaseClass):
	def __init__(self, value):
		#MyBaseClass.__init__(self, value)
		super().__init__(value)
		self.value += 2

class MyTimeFive(MyBaseClass):
	def __init__(self, value):
		#MyBaseClass.__init__(self, value)
		super().__init__(value)
		self.value *= 5

class MyClass1(MyAddTwo, MyTimeFive):
	def __init__(self, value):
		#MyAddTwo.__init__(self, value)
		#MyTimeFive.__init__(self, value)
		super().__init__(value)

class MyClass2(MyTimeFive, MyAddTwo):
	def __init__(self, value):
		#MyAddTwo.__init__(self, value)
		#MyTimeFive.__init__(self, value)
		super().__init__(value)

a = MyClass1(5)
b = MyClass2(5)
print(a.value)
print(b.value)
