import os

from concurrent import futures

import grpc
import time

import data_pb2, data_pb2_grpc
import pickle, base64

from mytest import MyClass

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '20001'

class DnetPredict(data_pb2_grpc.DnetPredictServicer):
    def dnet_detect(self, request, context):
        str = request.text
        print('Received data from client: ', str)
        #return data_pb2.Data(text = str.upper())
        my_class = base64.b64decode(str)
        my_class = pickle.loads(my_class)
        print('After decoding, my_class.value = ', my_class.value)
        my_class.value = os.getpid()
        str = pickle.dumps(my_class)
        str = base64.b64encode(str)

        return data_pb2.Data(text = str)

def server():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers = 4))
    data_pb2_grpc.add_DnetPredictServicer_to_server(DnetPredict(), grpcServer)
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)
    grpcServer.start()
    print("Service started. ")

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        print("Stop the service. ") 
        grpcServer.stop(0)

if __name__ == '__main__':
    server()

