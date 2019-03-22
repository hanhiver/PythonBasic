import numpy as np 

"""
InputArray: input array. 

Return: (pos, value)
	pos: index of the center possition. 
	value: value for the center position. 
"""
def getCenterPoint(inputArray):
	value = None

	length = inputArray.size
	if length == 0: 
		return (0, value)
	elif length == 1:
		return (0, inputArray[0])

	value = inputArray.max()

	begin = 0
	end = length - 1
	balance = 0
	balance += inputArray[begin]
	balance -= inputArray[end]

	while begin < end:
		if balance >= 0:
			end -= 1
			balance -= inputArray[end]
		else:
			begin += 1
			balance += inputArray[begin]

	return (begin, value)  

def lineSegment(inputArray, min_sep = 0):
	ret = []
	segment = []

	for item in inputArray:
		if item <= min_sep:
			if segment:
				ret.append(segment)
				segment = []
			continue
		else:
			segment.append(item)

	if segment:
		ret.append(segment)

	np.array(ret)
	return ret


def main():
	#a = [1]
	a = [6, 13,	34,	31,	54,	134, 165, 238, 
		 237, 232, 149, 176, 150, 86, 81, 
		 75, 78, 102, 67, 49, 33, 18, 19, 16, 8, 1]

	#a = [1, 15, 45, 67, 32, 2, 3, 2, 1]
	a = np.array(a)
	print(a)

	#pos, value = getCenterPoint(a)
	#print("Find center of the vect, pos: {}, value: {}. ".format(pos, value))

	res = lineSegment(a)
	print("After line segmentation: ")
	print(res)




if __name__ == '__main__':
	main()