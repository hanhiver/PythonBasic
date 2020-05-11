import array
import binascii
import tempfile

a = array.array('i', range(5))
print('Array A1: ', a)

output = tempfile.NamedTemporaryFile()
print('Write to file {}'.format(output.name))

a.tofile(output.file)
output.flush()

print('Read back from the file. ')
with open(output.name, 'rb') as input_file:
	raw_data = input_file.read()
	print('Raw data from the file: ', binascii.hexlify(raw_data))

	input_file.seek(0)
	a2 = array.array('i')
	a2.fromfile(input_file, len(a))
	print('Array A2: ', a2)