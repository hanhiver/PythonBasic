import multiprocessing 

from time import time, sleep

def run():
	start = time()
	sleep(1)

def main():
	start = time()

	process_list = []

	for i in range(3):
		t = multiprocessing.Process(target = run)
		process_list.append(t)

	for t in process_list:
		t.start()

	for t in process_list:
		t.join()

	print('Programm finished in {} seconds.'.format(time() - start))

if __name__ == '__main__':
	main()

