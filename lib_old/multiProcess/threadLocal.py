import threading 

# Create a ThreadLocal object. 
local_school = threading.local()

def process_student():
	# Get student that associate with current thread. 
	std = local_school.student 
	print('Hello, {} (in {})'.format(std, threading.current_thread().name()))

def process_thread():
	# Bind ThreadLocal.student. 
	local_school.student = name
	process_student()

t1 = threading.Thread(target = process_thread, args = ('Alice',), name = 'Thread-A')
t2 = threading.Thread(target = process_thread, args = ('Bob',), name = 'Thread-B')

t1.start()
t2.start()

t1.join()
t2.join()

