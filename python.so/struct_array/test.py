import ctypes

mylib = ctypes.cdll.LoadLibrary("libtest.so")

class Point(ctypes.Structure):
	_fields_ = [ ('x', ctypes.c_int), 
				 ('y', ctypes.c_int) ]

mylib.testlib()

point_array = Point * 3
points = point_array()

mylib.genPoint(ctypes.pointer(points), 3)
mylib.readPoint(ctypes.pointer(points), 3)
