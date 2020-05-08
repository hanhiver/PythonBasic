
a = [1.1, 2.2, 3.3]

with open('/tmp/test.txt', 'w') as file:
	for item in a:
		file.write(str(item) + '\n')

