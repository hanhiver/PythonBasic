import ctypes as ct 

so_file = './libtest.so'
lib = ct.cdll.LoadLibrary(so_file)

lib.test()

class mouse(ct.Structure):
    _fields_ = [('right', ct.c_int), ('left', ct.c_int)]

class computer(ct.Structure):
    _fields_ = [('my_screen', ct.c_int), ('my_mouse', mouse)]

"""
comp = computer()
comp.my_screen = 3
comp.my_mouse = mouse()
comp.my_mouse.right = 2
comp.my_mouse.left = 1
"""

ms = mouse(1, 2)
comp = computer(3, ms)

res = lib.read(ct.byref(comp))
res = lib.job(comp)
print('Return value: {}.'.format(res))

