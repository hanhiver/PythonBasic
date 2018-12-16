import random, time, queue
from multiprocessing.managers import BaseManager 

# Send task queue.
task_queue = queue.Queue()

# Receive task queue. 
result_queue = queue.Queue()

# QueueManager that inheite from BaseManager
class QueueManager(BaseManager):
	pass

def get_task_queue():
	global task_queue
	return task_queue

def get_result_queue():
	global result_queue
	return result_queue

# Register the two queue to the network. 
# Callable parameters will associate the queue objectives. 
#QueueManager.register('get_task_queue', callable = lambda: task_queue)
#QueueManager.register('get_result_queue', callable = lambda: result_queue)
QueueManager.register('get_task_queue', callable = get_task_queue)
QueueManager.register('get_result_queue', callable = get_result_queue)

# Bind to the 5000 port, set the passcode to 'abc'. 
manager = QueueManager(address = ('127.0.0.1', 5000), authkey = b'abc') 

# Start the queue. 
manager.start()

# Get the queue objects from network. 
task = manager.get_task_queue()
result = manager.get_result_queue()

# Add some task in to the queue. 
for i in range(10):
	n = random.randint(0, 100)
	print('Put task {} .. '.format(n))
	task.put(n)

# Get result from the result queue. 
print('Try get results...')
for i in range(10):
	r = result.get(timeout = 10)
	print('Result: {}'.format(r))

# Shutdown the queues. 
manager.shutdown()
print('Master exit.')
