import threading 

from time import time, sleep

def run():
	start = time()
	sleep(1)

def main():
	start = time()

	thread_list = []

	for i in range(3):
		t = threading.Thread(target = run)
		thread_list.append(t)

	for t in thread_list:
		t.start()

	for t in thread_list:
		t.join()

	print('Programm finished in {} seconds.'.format(time() - start))

if __name__ == '__main__':
	main()
	
