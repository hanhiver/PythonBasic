def count_number(input_str):
	result = []
	if not input_str:
		result.append(0)

	for index, letter in enumerate(input_str):
		#print(type(letter))
		if letter == ' ':
			result.append(index + 1)

	return result

def gen_count_number(input_str):
	if not input_str:
		yield 0

	for index, letter in enumerate(input_str):
		if letter == ' ':
			yield index + 1


if __name__ == '__main__':
	my_str = "Do you know that I love you so much!"

	print('Call the traditional function:')
	res = count_number(my_str)
	print(res)

	print('Call the generator version function: ')
	res = list(gen_count_number(my_str))
	print(res)
