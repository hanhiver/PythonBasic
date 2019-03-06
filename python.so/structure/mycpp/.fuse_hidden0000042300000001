import ctypes

mylib = ctypes.cdll.LoadLibrary("./cpptest.so")

class sub_struct(ctypes.Structure):
	_fields_ = [ ("test_int1", ctypes.c_int), 
				 ("test_int2", ctypes.c_int) ]

class struct_def(ctypes.Structure):
	_fields_ = [ ("test_int3", ctypes.c_int), 
				 ("son_struct", sub_struct) ] 

mystruct = struct_def()
mystruct.test_int3 = 3
mystruct.son_struct.test_int1 = 1
mystruct.son_struct.test_int2 = 2

#mylib.test_value(mystruct)
mylib.test_pointer(ctypes.byref(mystruct))
