import logging
import logging.handlers
import queue

que = queue.Queue()
queue_handler = logging.handlers.QueueHandler(que)
handler = logging.StreamHandler()

listener = logging.handlers.QueueListener(que, handler)

root = logging.getLogger()
root.addHandler(queue_handler)
formatter = logging.Formatter('%(asctime)s <%(threadName)s>: %(message)s')
handler.setFormatter(formatter)
listener.start()

root.warning('Look out!')
listener.stop()

