from concurrent import futures

import grpc
import data_pb2, data_pb2_grpc

#_HOST = 'localhost'
_HOST = 'dliforsup'
_PORT = '20001'
<<<<<<< HEAD
_TEXT = 'hello, world!' * 400000
=======
_TEXT = 'hello, world!' 
>>>>>>> 1d851238f26d64796720a9370a202a20ae3aeb0a

def run():
	conn = grpc.insecure_channel(_HOST + ':' + _PORT)
	client = data_pb2_grpc.FormatDataStub(channel = conn)
	print('Send: ' + _TEXT)
	response = client.DoFormat(data_pb2.Data(text = _TEXT))
	print('Received: ' + response.text)

if __name__ == '__main__':
	run()

