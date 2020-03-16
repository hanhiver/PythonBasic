def gen():
	yield 1
	yield 2
	yield 3

def gen2():
	for i in range(5):
		yield i 

for i in gen2():
	print(i)

