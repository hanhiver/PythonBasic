import ctypes as ct 

so_file = './libtest.so'
lib = ct.cdll.LoadLibrary(so_file)

lib.test()

class MOUSE(ct.Structure):
    _fields_ = [('right', ct.c_int), ('left', ct.c_int)]

class COMPUTER(ct.Structure):
    _fields_ = [('my_screen', ct.c_int), ('my_mouse', MOUSE)]

comp = COMPUTER()
comp.my_screen = 3
comp.my_mouse.right = 2
comp.my_mouse.left = 1

res = lib.job(comp)
print('Return value: {}.'.format(res))

