

a = 10
b = 20

def fun():
	a = 100
	b = 200
	for i in range(3):
		print(a)
		print(b)
		a += 1
		b += 1



def fun2():
	global a, b

	for i in range(3):
		print(a)
		print(b)
		a += 1
		b += 1

print(a, b)

fun()

print(a, b)

fun2()

print(a, b)

