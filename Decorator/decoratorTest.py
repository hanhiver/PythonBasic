import time 
import functools

def time_it(fn):
	print('time_it is executed')

	def new_fn(*args):
		start = time.time()
		result = fn(*args)
		end = time.time()
		duration = end - start 
		print("%s seconds are consumed in executing function: %s %r" 
			% (duration, fn.__name__, args))
		return result

	return new_fn

def time_it2(keep_meta = True):
	def real_dec(fn):
		if keep_meta:
			@functools.wraps(fn)
			def new_fn(*args):
				start = time.time()
				result = fn(*args)
				end = time.time()
				duration = end - start 
				print("%s seconds are consumed in executing function: %s %r" 
					% (duration, fn.__name__, args))
				return result
		else:
			def new_fn(*args):
				start = time.time()
				result = fn(*args)
				end = time.time()
				duration = end - start 
				print("%s seconds are consumed in executing function: %s %r" 
					% (duration, fn.__name__, args))
				return result
		return new_fn
	return real_dec 

@time_it
def acc1(start, end):
	print('acc1 start')
	s = 0
	for i in range(end-start):
		s += 1
	print('acc1 end')
	return s

def acc2(start, end):
	print('acc2 start')
	s = 0
	for i in range(end-start):
		s += 1
	print('acc2 end')
	return s

@time_it2(keep_meta = True)
def acc3(start, end):
	print('acc3 start')
	s = 0
	for i in range(end-start):
		s += 1
	print('acc3 end')
	return s

print(acc1)
print(acc2)
print(acc3)

if __name__ == '__main__':
	acc1(10, 1000000)
	acc2(10, 1000000)
	acc3(10, 1000000)

