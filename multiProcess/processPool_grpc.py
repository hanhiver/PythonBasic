import multiprocessing
import threading
import os, time, random

def real_task(value):
	print('Run task {} ({})...'.format(value, os.getpid()))
	start = time.time()
	time.sleep(1)
	result = (value + 1) * random.random()
	end = time.time()
	print('Task {} run {:.4f} seconds.'.format(os.getpid(), (end - start)))
	return result

class MyProcessPool(object):
	def __init__(self, pool_size = 1):
		self.pool_size = pool_size
		self.pool = multiprocessing.Pool(self.pool_size)
	
	def __del__(self):
		self.pool.close()
		self.pool.join()

	def run_task_async(self, func, args):
		queue = self.pool.apply_async(func, args)
		return queue

	def run_task_sync(self, func, args):
		queue = self.pool.apply_async(func, args)
		result = queue.get()
		return result

def get_result(mypool, func, args):
	queue = mypool.run_task_async(func, args)
	result = queue.get()
	return result

def main1():
	start = time.time()

	print('Parent process {}.'.format(os.getpid()))

	pool = MyProcessPool(4)

	thread_list = []

	for i in range(8):
		t = threading.Thread(target = get_result, args = (pool, real_task, (i, )) )
		thread_list.append(t)

	for t in thread_list:
		t.start()

	for t in thread_list:
		t.join()

	print('All child processes done in {:.4f} seconds.'.format(time.time() - start))

def main2():
	start = time.time()

	print('Parent process {}.'.format(os.getpid()))

	pool = MyProcessPool(4)

	thread_list = []

	for i in range(8):
		t = threading.Thread(target = pool.run_task_async, args = (real_task, (i, )) )
		thread_list.append(t)

	for t in thread_list:
		t.start()

	for t in thread_list:
		t.join()

	print('All child processes done in {:.4f} seconds.'.format(time.time() - start))


if __name__ == '__main__':
	main1()
