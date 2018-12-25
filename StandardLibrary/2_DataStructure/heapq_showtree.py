import math 
import heapq
from pprint import pprint

from io import StringIO

data = [19, 9, 4, 10, 11, 12, 5, 21, 2, 23, 17, 18, 3, 1]

def show_tree(tree, total_width = 36, fill = ' '):
	'''Pretty-print a tree'''
	output = StringIO()
	last_row = -1

	for i, n in enumerate(tree):
		if i: 
			row = int(math.floor(math.log(i + 1, 2)))
		else:
			row = 0

		if row != last_row:
			output.write('\n')

		columns = 2 ** row 
		col_width = int(math.floor(total_width / columns))
		output.write(str(n).center(col_width, fill))
		last_row = row

	print(output.getvalue())
	print('-' * total_width)
	print()

heap = []
print('random : ', data)
print()

for n in data:
	print('add {:>3}: '.format(n))
	heapq.heappush(heap, n)

show_tree(heap)

print('All         :', data)
print('3 largest   :', heapq.nlargest(3, data))
print('from sort   :', list(reversed(sorted(data)[-3:])))
print('3 smallest  :', heapq.nsmallest(3, data))
print('from sort   :', sorted(data)[:3])
pprint(heap)




