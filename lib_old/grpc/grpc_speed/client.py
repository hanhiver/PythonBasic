from concurrent import futures
from threading import Thread

from time import time
import grpc
import data_pb2, data_pb2_grpc

import pickle, base64
import cv2

import darkPool

#HOST = '9.111.158.180'
#HOST = '9.181.92.123'
HOST = 'localhost'
PORT = '18501'

#IMAGE = 'dog.jpg'
IMAGE = 'road.jpg'

THREADS = 1

class FeedImage(Thread):
    def __init__(self, func, args):
        Thread.__init__(self)
        self.func = func
        self.args = args
        start = time()
        self.result = self.func(*self.args)
        self.runtime = time() - start

    def get_result(self):
        try:
            return self.result
        except:
            return None

if __name__ == '__main__':
    
    client = darkPool.clientInit(host = HOST, port = PORT)
    image = cv2.imread(IMAGE)

    thread_list = []

    for i in range(THREADS):
        t = FeedImage(func = darkPool.clientDetect, args = (client, image))
        #t = Thread(target = darkPool.clientDetect, args = (client, image))
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        result = t.get_result()
        runtime = t.runtime
        t.join()

    #print(runtime, ' Result: ', type(result), len(result))
    

