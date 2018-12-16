def gen():
	yield 1
	yield 2
	yield 3

if __name__ == '__main__':
	x = gen()
	for i in x:
		print(i)
	
	