import ctypes

print("STARTED.")

mylib = ctypes.cdll.LoadLibrary('./librect.so')

mylib.test()

class Point(ctypes.Structure):
	_fields_ = [ ('x', ctypes.c_int), 
				 ('y', ctypes.c_int) ]

class Rect(ctypes.Structure):
	_fields_ = [ ('deep', ctypes.c_int),
				 ('lt', Point), 
				 ('rb', Point) ]

p = Point(1, 2)
mylib.printPoint(p)

box = Rect()
box.deep = 5
box.lt = Point(10, 20)
box.rb = Point(30, 40)
mylib.printRect(box)

print("FINISHED. ")

