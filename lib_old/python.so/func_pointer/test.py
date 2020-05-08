import ctypes

mylib = ctypes.cdll.LoadLibrary("libtest.so")

mylib.testlib()


# Call func in python. 
mylib.call_func(mylib.func_add)

# Transfer the python func to C type function pointer and pass to C lib. 
def my_add(a, b):
	return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
func = CMPFUNC(my_add)

mylib.call_func(func)

