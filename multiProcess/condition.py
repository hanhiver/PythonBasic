import threading 
import queue, time, random

class Goods: 
	def __init__(self):
		self.count = 0
	
	def add(self, num = 1):
		self.count += num 

	def sub(self):
		if self.count >= 0:
			self.count -= 1

	def empty(self):
		return self.count <= 0

class Producer(threading.Thread):
	def __init__(self, condition, goods, sleeptime = 0.01):
		threading.Thread.__init__(self)
		self.cond = condition
		self.goods = goods 
		self.sleeptime = sleeptime

	def run(self):
		cond = self.cond
		goods = self.goods

		while True:
			cond.acquire()
			goods.add()
			print("Number of goods: ", goods.count, " Producer thread. ")
			cond.notifyAll()
			cond.release()
			time.sleep(self.sleeptime)

class Consumer(threading.Thread):
	def __init__(self, condition, goods, sleeptime = 0.02):
		threading.Thread.__init__(self)
		self.cond = condition
		self.goods = goods 
		self.sleeptime = sleeptime

	def run(self):
		cond = self.cond
		goods = self.goods

		while True:
			time.sleep(self.sleeptime)
			cond.acquire()
			while goods.empty():
				cond.wait()
			goods.sub()
			print("Number of goods: ", goods.count, " Consumer thread. ")
			cond.release()

g = Goods()
c = threading.Condition()

pro = Producer(c, g)
pro.start()

con = Consumer(c, g)
con.start()



