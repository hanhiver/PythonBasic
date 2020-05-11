import os
from multiprocessing import Process, Queue
from time import sleep

import tkinter as tk
from tkinter import ttk 


class MainWindow(object):
	def __init__(self):
		#self.info_queue = queue 
		self.info_queue = Queue()

		self.root = tk.Tk()
		self.bt_start = ttk.Button(self.root, text = 'START', command = self.btStartAction)
		self.bt_stop = ttk.Button(self.root, text = 'STOP', command = self.btStopAction)

		self.producer_process = Process(target = self.producer, args = (self.info_queue, ))
		self.consumer_process = Process(target = self.consumer, args = (self.info_queue, ))

	def arrangeWindows(self):
		self.bt_start.pack(side = 'left')
		self.bt_stop.pack(side = 'left')

	def producer(self, queue):
		for i in range(10):
			print('Producer: <{}>'.format(i))
			queue.put(i)
			sleep(0.3)

	def consumer(self, queue):
		for i in range(10):
			res = queue.get()
			print('consumer: {}'.format(res))
			sleep(0.5)

	def btStartAction(self):
		print('START button action')
		if not self.producer_process.is_alive():
			self.producer_process.start()

		if not self.consumer_process.is_alive():
			self.consumer_process.start()

	def btStopAction(self):
		print('STOP button action')
		if self.producer_process.is_alive():
			self.producer_process.terminate()
			self.producer_process.join()

		if self.consumer_process.is_alive():
			self.consumer_process.terminate()
			self.consumer_process.join()

def main():
	#info_queue = Queue()
	mainWindow = MainWindow()
	mainWindow.arrangeWindows()

	tk.mainloop()

if __name__ == '__main__':
	main()


