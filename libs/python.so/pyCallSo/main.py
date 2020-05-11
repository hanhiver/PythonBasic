import ctypes

so = ctypes.cdll.LoadLibrary
lib = so('./cpp_so.so')

print('python call cpp so: ')
lib.my_add(2, 3)

