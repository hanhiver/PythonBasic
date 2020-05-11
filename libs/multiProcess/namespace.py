import multiprocessing

class Test():
	def __init__(self):
		self.value = 'Test Class'

	def output(self):
		print('Class: ', self.value)

def func(para):
	print('Process: ', para, para.z.value)
	para.z.output()

def main():
	my_manager = multiprocessing.Manager()
	my_global = my_manager.Namespace()

	my_global.x = 10
	my_global.y = 'my hello'
	my_global.z = Test()

	p = multiprocessing.Process(target = func, args = (my_global, ))
	p.start()

	print('Main: ', my_global, my_global.z.value)

	p.join()

if __name__ == '__main__':
	main()
