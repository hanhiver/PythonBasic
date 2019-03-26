import ctypes
import numpy as np

so_file = './libtest.so'

lib = ctypes.cdll.LoadLibrary(so_file)

lib.testlib()

a = [[1, 2, 3], [4, 5, 6]]

strides_type = ctypes.c_int * 2
strides = strides_type(3 * ctypes.sizeof(ctypes.c_int), 1 * ctypes.sizeof(ctypes.c_int))

shapes_type = ctypes.c_int * 2
shapes = shapes_type()
shapes[0] = 2
shapes[1] = 3

nparr = np.array(a, dtype = np.intc)
cbuf = np.ctypeslib.as_ctypes(nparr)
lib.matrix_add(cbuf, ctypes.byref(strides), ctypes.byref(shapes))






