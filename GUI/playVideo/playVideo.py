import tkinter as tk 
from tkinter import ttk 

import cv2
from PIL import Image, ImageTk
import numpy as np 
import time

from multiprocessing import Process, Queue
from threading import Thread

import mjpeg_stream 
#import queue

class MainWindow(object):

    def __init__(self):
        self.video_process = None
        self.update_thread = None
        self.imgQueue = Queue()

        self.root = tk.Tk()
        self.root.resizable(width = False, height = False)

        # Define the fm1 to contain the label which show the video
        self.fm1 = ttk.Frame(self.root)
        self.showLabel = tk.Label(self.fm1, width = 400, height = 300)
        
        # Define the fm2 to contain the three botton
        self.fm2 = ttk.Frame(self.root)
        self.bt_start = ttk.Button(self.fm2, text = '开始', 
                                   command = self.startButtonAction)
        self.bt_stop = ttk.Button(self.fm2, text = '停止',
                                  command = self.stopButtonAction)
        self.bt_config = ttk.Button(self.fm2, text = '配置')

        self._arrangeMainWindow()


    def _arrangeMainWindow(self):
        image = Image.open('./lena.jpg')
        image = image.resize((400, 300), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(image)
        self.showLabel['image'] = self.render
        self.showLabel.pack(side = 'top', expand = 'yes', padx = 10, pady = 10)
        self.fm1.pack()

        # Define the fm2 to contain the three botton
        self.bt_start.pack(side = 'left')
        self.bt_stop.pack(side = 'left')
        self.bt_config.pack(side = 'left')
        self.fm2.pack(side = 'top', pady = 10)

    def _showCamera(self, videoPath):
        capture = cv2.VideoCapture(0)

        def cc(capture):
            while True:
                ret, frame = capture.read()
                frame = cv2.flip(frame, 1)
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                img = Image.fromarray(cv2image)
                image_file = ImageTk.PhotoImage(img)
                self.showLabel.setImage(image_file)
                    
        t = threading.Thread(target = cc, args = (capture, ))
        t.start()

    def _updateThread(self):
        frame_index = 0
        while True:
            try:
                image = self.imgQueue.get()
                print('\rGet {} frame from the queue.'.format(frame_index), end = '')
                frame_index += 1
                image = image.resize((400, 300), Image.ANTIALIAS)
                self.render = ImageTk.PhotoImage(image)
                self.showLabel['image'] = self.render 
            except:
                print('Queue error.')
                raise
            time.sleep(0.001)

    def _startUpdateThread(self):
        if self.update_thread == None:
            self.update_thread = Thread(target = self._updateThread)

        if not self.update_thread.is_alive():
            self.update_thread.start()


    def _startVideoProcess(self, imagePath, imgQueue):
        if self.video_process == None:
            self.video_process = Process(target = self.send_video_to_queue, 
                        args = (imagePath, imgQueue))
            self.video_process.daemon = True

        if not self.video_process.is_alive():
            self.video_process.start()

    def startButtonAction(self):
        '''
        image = Image.open('./dog.jpg')
        image = image.resize((400, 300), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(image)
        self.showLabel['image'] = self.render 
        '''
        imagePath = '/Users/dhan/Documents/myprog/python/highway/1_part.avi'
        self._startVideoProcess(imagePath, self.imgQueue)
        print('Video process started. ')

        self._startUpdateThread()
        print('update thread started. ')
        

    def stopButtonAction(self):
        if self.video_process.is_alive():
            self.video_process.terminate()
            self.video_process.join()

        #if self.update_thread.is_alive():
        #   self.update_thread.terminate()
        #   self.update_thread.join()

    def send_video_to_queue(self, videoPath, queue):
        vid = cv2.VideoCapture(videoPath)
        if not vid.isOpened():
            raise IOError("Couldn't open webcam or video")

        frame_index = 0

        while True:
            return_value, frame = vid.read()
            if return_value:
                frame[:, :, [0, 2]] = frame[:, :, [2, 0]]
                image = Image.fromarray(frame)
                #image = image.convert('L')
                queue.put(image)
                print('\rSent the {} frame'.format(frame_index), end = '')
                frame_index += 1
                time.sleep(0.001)
            else:
                print('End of the video file. ')
                break

def main():
    main_window = MainWindow()
    tk.mainloop()

if __name__ == '__main__':
    imgQueue = Queue()
    main()

