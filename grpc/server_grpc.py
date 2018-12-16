from concurrent import futures

import grpc
import time

import data_pb2, data_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '20001'

class FormatData(data_pb2_grpc.FormatDataServicer):
    def DoFormat(self, request, context):
        str = request.text
        print('Received data from client: ', str)
        return data_pb2.Data(text = str.upper())

def server():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers = 4))
    data_pb2_grpc.add_FormatDataServicer_to_server(FormatData(), grpcServer)
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

