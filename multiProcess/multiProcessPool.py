from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task {} ({})...'.format(name, os.getpid()))
	start = time.time()
	time.sleep(random.random())
	end = time.time()
	print('Task {} run {:2f} seconds.'.format(name, (end - start)))

if __name__ == '__main__':
	start = time.time()

	print('Parent process {}.'.format(os.getpid()))

	p = Pool(4)
	#p = Pool()

	for i in range(10):
		p.apply_async(long_time_task, args=(i, ))

	print('Waiting for all child processes done...')

	p.close()
	p.join()

	print('All child processes done in {} seconds.'.format(time.time() - start))

