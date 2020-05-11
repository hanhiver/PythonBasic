import multiprocessing
import os

from time import sleep

class Worker(object):
	def __init__(self):
		self.processInit()

	def processInit(self):
		sleep(1)
		print('Process <{}> initilized. '.format(os.getpid))

	def doWork(self, sleep_time):
		sleep(sleep_time)
		return os.getpid()

class WorkerPool(object):
	def __init__(self):
		self.pro_pool = []

	def workerProcess(): 