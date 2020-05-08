from multiprocessing.managers import BaseManager

class QueueManager(BaseManager): 
    pass

QueueManager.register('get_queue')

m = QueueManager(address=('dhan.org', 50000), authkey=b'abcabc')

m.connect()
queue = m.get_queue()

queue.get()
