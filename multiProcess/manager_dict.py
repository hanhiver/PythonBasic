import multiprocessing
import os

PROCESS_NUMBER = 3

def run(info_dict, info_list, lock):
	#lock.acquire()
	print('WORK: {}'.format(os.getpid()))
	info_dict[os.getpid()] = os.getpid()
	info_dict['PROCESS_LIST'].append(os.getpid())
	#info_list.append(os.getpid())
	print('WORK: {} DICT: '.format(os.getpid()), info_dict)
	print('WORK: {} LIST: '.format(os.getpid()), info_list)
	print('WORK: {} MIN: '.format(os.getpid()), info_list.index(min(info_list)))
	#lock.release()

def main():
	lock = multiprocessing.Lock()
	manager = multiprocessing.Manager()
	info_dict = manager.dict()
	info_list = manager.list()

	info_dict['PROCESS_LIST'] = info_list

	process_list = []

	for i in range(PROCESS_NUMBER):
		p = multiprocessing.Process(target = run, args = (info_dict, info_list, lock))
		process_list.append(p)
		p.start()

	for p in process_list:
		p.join()

	print(info_dict)
	print(info_list)

if __name__ == '__main__':
	main()
