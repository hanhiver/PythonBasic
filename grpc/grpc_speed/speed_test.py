
import os
import multiprocessing, threading
import cv2
import numpy as np 
from pprint import pprint
from time import time, sleep

import grpc
import data_pb2, data_pb2_grpc
import pickle, base64
from concurrent import futures


#####################
# Server part code. #
#####################

'''
Using the multiprocessing model to start moder server. 
'''

'''
Model Initialization. 
'''
def initialModel():
    print('WORKOR: {}, model initialed. '.format(os.getpid()))


'''
Feed image to the model. 

image: 
    cv2 images. 

Return: 
    Queue of model output. Use .get() to get the model output. 

'''
def feedImage(my_input):
    #print('WORKOR: {}, start to predict Image.'.format(os.getpid()))
    start = time()
    sleep(1)
    print('WORKOR: {}, complet a task in {:.5f} seconds.'.format(os.getpid(), time() - start))
    return my_input


'''
Model server process. 
'''
class ServerProcessPool(object):
    def __init__(self, pool_size = 1):
        self.pool_size = pool_size
        self.pool = multiprocessing.Pool(processes = pool_size, 
                                         initializer = initialModel)

    def __del__(self):
        self.pool.close()
        self.pool.join()

    def predictImage(self, image):
        res = self.pool.apply_async(feedImage, (image, ))
        return res 

'''
grpc Services for model process.
'''
class DnetPredict(data_pb2_grpc.DnetPredictServicer):
    def __init__(self, model_pool_size = 1):
        self.model_pool = ServerProcessPool(pool_size = model_pool_size)

    def dnet_detect(self, request, context):
        
        start = time()

        str = request.text
        image = base64.b64decode(str)
        image = pickle.loads(image)        
        return_queue = self.model_pool.predictImage(image)
        result = return_queue.get()
        result = pickle.dumps(result)
        result = base64.b64encode(result)

        #print('WORKOR: {} done one image in: {}'.format(os.getpid(), time() - start))
        
        return data_pb2.Data(text = result)
'''
Start the grpc server. 
host: 
    grpc server host. 

port: 
    grpc server port.

model_pool_size: 
    how many process in the server pool to provide model service. 
'''
def startServer(port = _PORT, 
                model_pool_size = 1,
                send_msg_size = _SERVER_SEND_MSG_SIZE, 
                recv_msg_size = _SERVER_RECV_MSG_SIZE):
    serverOptions = [('grpc.max_send_message_length', send_msg_size),
                     ('grpc.max_receive_message_length', recv_msg_size)]
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers = model_pool_size * 3), options = serverOptions)
    data_pb2_grpc.add_DnetPredictServicer_to_server(DnetPredict(model_pool_size = model_pool_size), grpcServer)
    grpcServer.add_insecure_port('[::]:' + port)
    grpcServer.start()
    print('Server Started: send_msg_size/recv_msg_size: {}/{}'.format(send_msg_size, recv_msg_size))

    try:
        while True:
            sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        print("Stop the service. ") 
        grpcServer.stop(0)


#####################
# Client Part code. #
#####################

'''
Initialize process in client side, connect the grpc server.  
host: 
    grpc server host. 

port: 
    grpc server port. 

Return: 
    grpc client for client call. 
'''
def clientInit(host = _HOST, 
               port = _PORT, 
               send_msg_size = _SERVER_RECV_MSG_SIZE, 
               recv_msg_size = _SERVER_SEND_MSG_SIZE):
    clientOptions = [('grpc.max_send_message_length', send_msg_size), 
                     ('grpc.max_receive_message_length', recv_msg_size)]
    conn = grpc.insecure_channel(host + ':' + port, options = clientOptions)
    client = data_pb2_grpc.DnetPredictStub(channel = conn)
    print('Creat client: send_msg_size/recv_msg_size: {}/{}'.format(send_msg_size, recv_msg_size))

    return client

'''
Send image to the model server for prediction. 
client: 
    grpc client from the clientInit()

image: 
    cv2 image that need to be sent to the model.

Return: 
    prediction result from the model. 
    In this darknet server it contains: out_boxes, out_scores, out_classes
'''
def clientDetect(client, image):
    message = pickle.dumps(image)
    message = base64.b64encode(message)
    print('Send a image to model. ')
    response = client.dnet_detect(data_pb2.Data(text = message))
    result = response.text
    result = base64.b64decode(result)
    result = pickle.loads(result)
    #print('Received result. ', result)
    return result


'''
Example. 
'''
def main():
    ppool = ServerProcessPool(pool_size = 1)
    image = cv2.imread('dog.jpg')

    res = ppool.predictImage(image)
    out_boxes, out_scores, out_classes = res.get()

    pprint(out_classes)
    pprint(out_scores)
    pprint(out_boxes)

    from PIL import Image, ImageDraw
    image = Image.fromarray(image)
    draw = ImageDraw.Draw(image)
    for item in out_boxes:
        top, left, bottom, right = item
        draw.rectangle([left, top, right, bottom], outline = (255, 255, 255), width = 3)

    del draw

    cv2.namedWindow("result", cv2.WINDOW_NORMAL)
    result = np.asarray(image)
    cv2.imshow("result", result)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()


if __name__ == '__main__':
    #main()
    startServer(model_pool_size = 1)
