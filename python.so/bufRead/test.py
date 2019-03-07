import ctypes
import numpy as np

so_file = './libtest.so'

lib = ctypes.cdll.LoadLibrary(so_file)

lib.testlib()

print("\n=== String Test ===")

buf = ctypes.create_string_buffer(20)
ctypes.cast(buf, ctypes.c_void_p)

lib.wbuf(buf, 20)
lib.rbuf(buf, 20)

pybuf = (ctypes.c_char * 20).from_buffer_copy(buf)
print('BUFFER Content: ', pybuf.value.decode())
pydata = list(pybuf)
print('PYDATA: ', pydata)

"""
print("=== Matrix Test (Numpy) ===")
matrix = np.zeros((2, 3), np.int)

lib.matrix_write.restype = ctypes.c_int
lib.matrix_write.argtypes = [np.ctypeslib.ndpointer(dtype = np.int, ndim = 2), 
							 ctypes.POINTER(ctypes.c_long * 2), 
							 ctypes.POINTER(ctypes.c_long * 2)]
def my_mwrite(x):
	return lib.matrix_write(x, x.ctypes.strides, x.ctypes.shape)


print("Before: ", repr(matrix))

my_mwrite(matrix)

print("After: ", repr(matrix))
"""

print("\n=== Matrix Test ===")

mbuf = ctypes.create_string_buffer(ctypes.sizeof(ctypes.c_int) * 6)
ctypes.cast(mbuf, ctypes.c_void_p)

strides_type = ctypes.c_int * 2
strides = strides_type(3 * ctypes.sizeof(ctypes.c_int), 1 * ctypes.sizeof(ctypes.c_int))

shapes_type = ctypes.c_int * 2
shapes = shapes_type()

shapes[0] = 2
shapes[1] = 3

lib.matrix_write(mbuf, strides, shapes)
lib.matrix_add(mbuf, ctypes.byref(strides), ctypes.byref(shapes))

pybuf = (ctypes.c_int * 6).from_buffer(mbuf)
pydata = list(pybuf)
print('PYDATA: ', pydata)

npdata = np.array(pybuf, dtype = np.int32)
print('NPDATA: {} \n shape: {}'.format(npdata, npdata.shape))
npdata = npdata.reshape((2, 3))
print('NPDATA: {} \n shape: {}'.format(npdata, npdata.shape))

npdata_as = np.ctypeslib.as_array(pybuf)
print('NPDATA_AS: {} \n shape: {}'.format(npdata_as, npdata_as.shape))
npdata_as = npdata_as.reshape((2, 3))
print('NPDATA_AS: {} \n shape: {}'.format(npdata_as, npdata_as.shape))



print("\n=== C buffer Test ===")
cbuf = ctypes.c_void_p()
lib.create_matrix(ctypes.byref(cbuf), 6 * ctypes.sizeof(ctypes.c_int))

lib.matrix_write(cbuf, strides, shapes)
lib.matrix_add(cbuf, ctypes.byref(strides), ctypes.byref(shapes))

cbuf2 = ctypes.cast(cbuf, ctypes.POINTER(ctypes.c_int))
npdata_as = np.ctypeslib.as_array(cbuf2, shape = (6, ))
print('NPDATA_AS: {} \n shape: {}'.format(npdata_as, npdata_as.shape))
npdata_as = npdata_as.reshape((2, 3))
print('NPDATA_AS: {} \n shape: {}'.format(npdata_as, npdata_as.shape))


"""
cbuf2 = ctypes.cast(cbuf, ctypes.POINTER(ctypes.c_int))
pycbuf = (ctypes.c_int).from_buffer_copy(cbuf2)
pycdata = list(pycbuf)
print('PYCDATA: ', pycdata)

npcdata = np.array(pycbuf, dtype = np.int32)
print('NPCDATA: {} \n shape: {}'.format(npdata, npdata.shape))
npcdata = npcdata.reshape((2, 3))
print('NPCDATA: {} \n shape: {}'.format(npdata, npdata.shape))
"""


#ctypes.cast(mbuf, ctypes.POINTER(ctypes.c_int))

#np_matrix = np.ctypeslib.as_array(mbuf)
#print('MBUFFER Content: ', repr(np_matrix))

#myarray = np.ctypeslib.as_array(pybuf, shape = (2, 3))
#print(repr(myarray))




