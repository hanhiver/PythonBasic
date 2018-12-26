import subprocess 
from time import time

def run_sleep(period):
	print('Run a subprocess')
	proc = subprocess.Popen(['sleep', str(period)])
	return proc

def run_openssl(data):
	env = os.environ.copy()
	env['password'] = b'dhan'
	proc = subprocess.Popen

if __name__ == '__main__':
	start = time()
	procs = []

	for _ in range(10):
		proc = run_sleep(0.1)
		procs.append(proc)

	for proc in procs:
		proc.communicate()

	end = time()

	print('Finished in {} seconds'.format(end - start))
