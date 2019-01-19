from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_queue')

m = QueueManager(address = ('localhost', 50000), authkey = b'abcabc')
m.connect()

queue = m.get_server()
queue.put('hello')

