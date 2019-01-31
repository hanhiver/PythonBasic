import multiprocessing
import threading
import os, time, random

class MyProcess(multiprocessing.Process):
	def __init__(self, func, args):
		multiprocessing.Process.__init__(self)
		self.result = func(*args)

def long_time_task(value):
	print('Run task {} ({})...'.format(value, os.getpid()))
	start = time.time()
	time.sleep(1)
	result = (value + 1) * random.random()
	end = time.time()
	print('Task {} run {:.4f} seconds.'.format(os.getpid(), (end - start)))
	return result

def get_result(pool, args):
	result_queue = pool.apply_async(long_time_task, args)
	result = result_queue.get()
	return result

def main1():
	start = time.time()

	print('Parent process {}.'.format(os.getpid()))

	pool = multiprocessing.Pool(4)

	thread_list = []

	for i in range(8):
		t = threading.Thread(target = get_result, args = (pool, (i, )))
		thread_list.append(t)

	for t in thread_list:
		t.start()

	for t in thread_list:
		t.join()


	pool.close()
	pool.join()

	print('All child processes done in {:.4f} seconds.'.format(time.time() - start))


if __name__ == '__main__':
	main1()
