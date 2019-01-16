from concurrent import futures

import grpc
import data_pb2, data_pb2_grpc

import pickle, base64
from mytest import MyClass


_HOST = 'localhost'
_PORT = '20001'
_TEXT = 'hello, world!' 

def run():
    myclass = MyClass(3)
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = data_pb2_grpc.DnetPredictStub(channel = conn)
    #print('Send: ' + _TEXT)
    print('Send, my_class.value = ', myclass.value)
    message = pickle.dumps(myclass)
    message = base64.b64encode(message)
    response = client.dnet_detect(data_pb2.Data(text = message))
    result = response.text
    result = base64.b64decode(response.text)
    result = pickle.loads(result)
    print('Received, my_class.value = ', result.value)
    #print('Received: ' + response.text)

if __name__ == '__main__':
    run()

