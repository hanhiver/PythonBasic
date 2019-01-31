import sys
import threading
import multiprocessing

import loggerManager

logger_manager = None

def write_log():
	global logger_manager
	logger = logger_manager.get_logger('write_log')
	logger.debug('A DEBUG infomation in thread. ')
	logger.info('A INFO information in thread. ')

def main():
	global logger_manager

	#log_filename = sys.argv[0].split('.')[0] + '.log'
	logger_manager = loggerManager.LoggerManager()

	logger = logger_manager.get_logger('main')
	logger.debug('A DEBUG information in Main. ')
	logger.info('A INFO information in Main. ')

	thread_list = []

	for i in range(4):
		t = threading.Thread(target = write_log)
		thread_list.append(t)
		t.start()

	for t in thread_list:
		t.join()

	process_list = []

	for i in range(4):
		p = multiprocessing.Process(target = write_log)
		process_list.append(p)
		p.start()

	for p in process_list:
		p.join()

	logger_manager.stop()


if __name__ == '__main__':
	main()

