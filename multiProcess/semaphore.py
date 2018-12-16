import threading
import time

class Num:
	def __init__(self):
		self.num = 0
		# Allow max 3 threads to access the resource. 
		self.sem = threading.Semaphore(value = 3)

	def add(self):
		self.sem.acquire()
		self.num += 1
		num = self.num 
		self.sem.release()
		return num 

n = Num()

class jdThread(threading.Thread):
	def __init__(self, item):
		threading.Thread.__init__(self)
		self.item = item 

	def run(self):
		time.sleep(0.02)
		value = n.add()
		print(self.item, value)

for item in range(100):
	t = jdThread(item)
	t.start()
	t.join()



		