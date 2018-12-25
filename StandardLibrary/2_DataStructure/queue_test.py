import threading 
from queue import Queue
from time import sleep 

def Producer(input_queue):
	for i in range(5):
		input_queue.put(i)
		print('Producer: <', i, '> ', threading.currentThread().name)
		sleep(0.1)

def Consumer(output_queue):
	for i in range(5):
		res = output_queue.get()
		print('Consumer: <', res, '> ', threading.currentThread().name)
		sleep(0.2)

my_queue = Queue()

t1 = threading.Thread(target = Producer, args = (my_queue, ), name = 'Producer Thread1')
t2 = threading.Thread(target = Consumer, args = (my_queue, ), name = 'Consumer Thread1')
t3 = threading.Thread(target = Producer, args = (my_queue, ), name = 'Producer Thread2')
t4 = threading.Thread(target = Consumer, args = (my_queue, ), name = 'Consumer Thread2')

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
