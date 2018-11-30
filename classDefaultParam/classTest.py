class Test:

	_defaults = {
		"TEST_PARAM1" : 10,
		"TEST_PARAM2" : "hello",
	}

	@classmethod
	def get_default(cls, n):
		if n in cls._defaults:
			return cls._defaults[n]
		else:
			return "Unrecognized attribute name '" + n + "'"

	def __init__(self, **kwargs):
		self.__dict__.update(self._defaults)
		self.__dict__.update(kwargs)

	def printParams(self):
		print("TEST_PARAM1 = {}".format(self.TEST_PARAM1))
		print("TEST_PARAM2 = {}".format(self.TEST_PARAM2))


if __name__ == '__main__':
	ct1 = Test()
	ct1.printParams()

	ct2 = Test(TEST_PARAM1=20, TEST_PARAM2='world')
	ct2.printParams()

	ct3 = Test(TEST_PARAM3='Ops...', TEST_PARAM1=Test.get_default("TEST_PARAM1")-2)
	print(ct3.TEST_PARAM3)
	print(ct3.TEST_PARAM1)
	print(ct3.get_default("TEST_PARAM1"))
	print(ct3.get_default("TEST_PARAM3"))




