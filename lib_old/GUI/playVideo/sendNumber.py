import tkinter as tk 
from tkinter import ttk 

import cv2
from PIL import Image, ImageTk
import numpy as np 
import time
from random import random
from time import sleep

from multiprocessing import Process, Queue
from threading import Thread 
#import queue



class MainWindow(object):

	def __init__(self):
		self.video_process = None
		self.update_process = None
		self.imgQueue = Queue()

		self.root = tk.Tk()
		self.root.resizable(width = False, height = False)

		# Define the fm1 to contain the label which show the video
		self.fm1 = ttk.Frame(self.root)
		self.showLabel = tk.Label(self.fm1)
		
		# Define the fm2 to contain the three botton
		self.fm2 = ttk.Frame(self.root)
		self.bt_start = ttk.Button(self.fm2, text = '开始', 
						           command = self.startButtonAction)
		self.bt_stop = ttk.Button(self.fm2, text = '停止',
								  command = self.stopButtonAction)
		self.bt_config = ttk.Button(self.fm2, text = '配置')

		self._arrangeMainWindow()


	def _arrangeMainWindow(self):
		'''
		image = Image.open('./lena.jpg')
		image = image.resize((400, 300), Image.ANTIALIAS)
		self.render = ImageTk.PhotoImage(image)
		self.showLabel['image'] = self.render
		'''
		self.showLabel['text'] = str(42)
		self.showLabel.pack(side = 'top', padx = 10, pady = 10)
		self.fm1.pack(side = 'top')

		# Define the fm2 to contain the three botton
		self.bt_start.pack(side = 'left')
		self.bt_stop.pack(side = 'left')
		self.bt_config.pack(side = 'left')
		self.fm2.pack(side = 'top', pady = 10)

	def _updateThread(self):
		while True:

			sentValue = self.imgQueue.get()
			print('Get value from the queue: ', sentValue)
			self.showLabel['text'] = str(sentValue)

			time.sleep(0.5)

	def _startUpdateThread(self):
		if self.update_process == None:
			self.update_process = Thread(target = self._updateThread)

		if not self.update_process.is_alive():
			self.update_process.start()

	def _videoProcess(self):
		while True:

			sendValue = random()
			self.imgQueue.put(sendValue)
			print('Sent value: ', sendValue)

			sleep(0.5)

	def _startVideoProcess(self):
		if self.video_process == None:
			self.video_process = Process(target = self._videoProcess)
		if not self.video_process.is_alive():
			self.video_process.start()

	def startButtonAction(self):
		self._startUpdateThread()
		print('update process started. ')
		self._startVideoProcess()
		print('video process started. ')

	def stopButtonAction(self):
		if self.video_process.is_alive():
			self.video_process.terminate()
			self.video_process.join()

		if self.update_process.is_alive():
			self.update_process.terminate()
			self.update_process.join()


def main():
	main_window = MainWindow()
	tk.mainloop()

if __name__ == '__main__':
	imgQueue = Queue()
	main()

