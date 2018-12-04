import time, sys, queue

from multiprocessing.managers import BaseManager

# Create QueueManager from BaseManager. 
class QueueManager(BaseManager):
	pass

# This QueueManager only get queues from the network, 
# so, we only provide the register name. 
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# Connect to the servier which run multiprocess_server.py. 
server_addr = '127.0.0.1'
print('Connect to the server {}...'.format(server_addr))

# Make sure the authkey is the same in server side. 
m = QueueManager(address = (server_addr, 5000), authkey = b'abc')

# Connect the network. 
m.connect()

# Get the queues. 
task = m.get_task_queue()
result = m.get_result_queue()

# Get tasks from the task_queue and fill the result to result_queue. 
for i in range(10):
	try: 
		n = task.get(timeout = 1)
		print('run task {} * {} ... '.format(n, n))
		r = '{} * {} = {}'.format(n, n, n*n)
		time.sleep(0.02)
		result.put(r)
	except Queue.Empty: 
		print('task queue is empty.')

print('worker exit.')

