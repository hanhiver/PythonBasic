import multiprocessing
import os, time, random

class MyProcess(multiprocessing.Process):
	def __init__(self, func, args):
		super().__init__(self)
		self.result = func(*args)


def long_time_task(name):
	print('Run task {} ({})...'.format(name, os.getpid()))
	start = time.time()
	time.sleep(1)
	end = time.time()
	print('Task {} run {:.4f} seconds.'.format(name, (end - start)))

def main1():
	start = time.time()

	print('Parent process {}.'.format(os.getpid()))

	process_list = []

	for i in range(4):
		p = MyProcess(func = long_time_task, args = (str(i), ))
		process_list.append(p)

	for p in process_list:
		p.start()
		print('Result = ', p.result)
	
	print('Waiting for all child processes done...')

	p.close()
	p.join()

	print('All child processes done in {:.4f} seconds.'.format(time.time() - start))

def main2():
	start = time.time()

	print('Parent process {}.'.format(os.getpid()))

	p = multiprocessing.Pool(4)
	#p = Pool()

	for i in range(10):
		p.apply_async(long_time_task, args=(i, ))

	print('Waiting for all child processes done...')

	p.close()
	p.join()

	print('All child processes done in {:.4f} seconds.'.format(time.time() - start))

if __name__ == '__main__':
	main1()
