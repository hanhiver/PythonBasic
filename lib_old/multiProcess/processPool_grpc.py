import multiprocessing
import threading
import os, time, random

_MAX_PROCESSES_PER_GPU = 6

def process_init(pool_info, lock):
	print('Task: {} initialed.'.format(os.getpid()))
	pool_info['PROCESS_LIST'].append(os.getpid())
	print('Task: {} pool_info: {} \n\t Process List: {} \n\t GPU Affinity: {}'.format(os.getpid(), pool_info, pool_info['PROCESS_LIST'], pool_info['GPU_AFFINITY']))

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

		self.lock = multiprocessing.Lock()

		self.lock.acquire()

		with os.popen('nvidia-smi -L | grep GPU | wc -l') as command_pipe:
			gpu_number = command_pipe.read()
			gpu_number = int(gpu_number)
			print('GPU NUMBER:', gpu_number)

		self.manager = multiprocessing.Manager()
		self.pool_info = self.manager.dict()
		self.process_list = self.manager.list()
		self.gpu_affinity = self.manager.list()

		self.pool_info['GPU_NUMBER'] = gpu_number
		self.pool_info['MAX_PROCESSES_PER_GPU'] = _MAX_PROCESSES_PER_GPU
		self.pool_info['GPU_AFFINITY'] = self.gpu_affinity

		for i in range(4):
			self.gpu_affinity.append(0)
		
		self.pool_info['PROCESS_LIST'] = self.process_list

		print('Main Process Initialized. ')

		self.lock.release()

		self.pool = multiprocessing.Pool(processes = self.pool_size, 
										 initializer = process_init,
										 initargs = (self.pool_info, self.lock, ))
	
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
