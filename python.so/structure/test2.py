import ctypes as ct 


so_file = './libtest.so'
lib = ct.cdll.LoadLibrary(so_file)

print("1")

lib.test()

print("2")

class MOUSE(ct.Structure):
    _fields_ = [('right', ct.c_int), ('left', ct.c_int)]

print("3")

class COMPUTER(ct.Structure):
    _fields_ = [('my_screen', ct.c_int), ('my_mouse', MOUSE)]

print("4")

comp = COMPUTER()
comp.my_screen = 3
comp.my_mouse.right = 2
comp.my_mouse.left = 1

print("5")

res = lib.job(comp)

print("6")

print('Return value: {}.'.format(res))

