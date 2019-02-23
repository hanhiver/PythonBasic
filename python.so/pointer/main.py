import ctypes 

so_file = './libpointer.so'
lib = ctypes.cdll.LoadLibrary(so_file)

a = ctypes.c_int(125)
b = ctypes.c_char_p(b'Hello, in libpointer.so.')

class testpointer(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_char_p)]

t = testpointer()
t.a = a
t.b = b

lib.test.restype=ctypes.POINTER(testpointer)

t1 = lib.test(ctypes.byref(t))
print(t1.contents.a)
print(t1.contents.b)


