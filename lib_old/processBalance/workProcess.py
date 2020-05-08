import multiprocessing
import logging
import sys
import os

class MyWorker(multiprocessing.Process):
	def __init__(self, msg):
		super().__init__()
		self.my_string = 'Dongdong ' + msg 

	def run(self):
		print('PID <{}>, my messages: {}.'.format(os.getpid(), self.my_string))
		return


def worker():
	print("Do something. ")
	sys.stdout.flush()

if __name__ == '__main__':
	'''
	multiprocessing.log_to_stderr(logging.INFO)
	p = multiprocessing.Process(target = worker)
	p.start()
	p.join()
	'''

	jobs = []

	for i in range(5):
		p = MyWorker(str(i))
		jobs.append(p)
		p.start()

	for j in jobs:
		j.join()


