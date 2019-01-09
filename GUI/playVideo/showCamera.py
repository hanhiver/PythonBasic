import cv2
import tkinter as tk
from tkinter import filedialog 
from PIL import Image, ImageTk 
import threading 


# Create the Windows. 
#####################
windows = tk.Tk()
windows.title('Camera')

# Get the width and height of the screen. 
sw = windows.winfo_screenwidth()
sh = windows.winfo_screenheight()

wx = 600
wh = 800

# Place the windows to a certain position. 
windows.geometry('%dx%d+%d+%d' % (wx, wh, (sw-wx)/2, (sh-wh)/2-100))

# Draw the canvas. 
canvas = tk.Canvas(windows, bg = '#c4c2c2', 
	               height = wh, width = wx)
canvas.pack()

# Open the camera to get images. 
################################
def video_demo():
	capture = cv2.VideoCapture(0)

	def cc(capture):
		#capture = cv2.VideoCapture(0)
		while True:
			ret, frame = capture.read()
			frame = cv2.flip(frame, 1)
			cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
			img = Image.fromarray(cv2image)
			image_file = ImageTk.PhotoImage(img)
			canvas.create_image(0, 0, anchor = 'nw', image = image_file)
	
	t = threading.Thread(target = cc, args = (capture, ))
	t.start()

# Define a botton to start the image show. 
##########################################
bt_start = tk.Button(windows, text = 'Open Camera', 
	                 height = 2, width = 15, 
	                 command = video_demo)
bt_start.place(x = 230, y = 600)
tk.mainloop()

import sys
import time
 
for i in range(10000):
	percent = 1.0 * i / 10000 * 100
	print('complete percent:' + str(percent) + ‘%’, sys.stdout.write('\r'))
   	time.sleep(0.01)



