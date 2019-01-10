import multiprocessing
import os

def do_caculate(data):
	print('Worker {}: '.format(os.getpid()))
	return data * 2

def start_process():
	print('Initialize the work {}: '.format(os.getpid()))

if __name__ == '__main__':
	inputs = list(range(10))

	builtin_output = list(map(do_caculate, inputs))
	print('Built-in: ', builtin_output)

	print('\n\n\n')

	pool_size = multiprocessing.cpu_count() * 2
	pool_size = 4 
	pool = multiprocessing.Pool(processes = pool_size, 
								initializer = start_process)

	pool_outputs = pool.map(do_caculate, inputs)
	pool.close()
	pool.join()

	print('Pool:     ', pool_outputs)

