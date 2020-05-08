""" Python version of quick sort. 
	Dong Han 2018.10.29 for fun. """

def quickSort(array):

	if (len(array) <= 1):
		return array

	midValue = array[ (len(array) // 2) ]

	left = [ x for x in array if x < midValue ]
	middle = [ x for x in array if x == midValue ]
	right = [ x for x in array if x > midValue ]

	return quickSort(left) + middle + quickSort(right)

if __name__ == '__main__':
	array = [4, 5, 8, 0, 1, 4, 6, 7, 10, 45, 3, -2, -8]
	print("\033[0;31m%s\033[0m" % "Before the sort: ")
	print(array)
	print("\033[0;31m%s\033[0m" % "After quicksort:")
	print(quickSort(array))
