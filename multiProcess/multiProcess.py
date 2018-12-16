# -*- coding: utf-8 -*-
from multiprocessing import Process
import os

def run_proc(name):
	#print('运行子进程 {} ({})...'.format(name, os.getpid()))
	print('Run the child process: {} ({})...'.format(name, os.getpid()))
	

if __name__ == '__main__':
	#print('父进程 {}.'.format(os.getpid()))
	print('Father process: {}.'.format(os.getpid()))

	p = Process(target = run_proc, args = ('test', ))

	print('Starting the child process.')
	#print('子进程将要启动。')

	p.start()
	p.join()

	#print('子进程结束。')
	print('Child process ended.')

