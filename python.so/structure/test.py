import ctypes as ct 

so_file = './libtest.so'
lib = ct.cdll.LoadLibrary(so_file)

lib.test()

#class mouse(ct.Structure):
#    _fields_ = [('right', ctypes.c_int), ('left', ct.c_int)]

class computer(ct.Union):
    class mouse(ct.Structure):
        _fields_ = [('right', ct.c_int), ('left', ct.c_int)]

    #_anonymous_ = ('my_mouse', )
    _fields_ = [('my_screen', ct.c_int), ('my_mouse', mouse)]

test_computer = computer()
test_computer.my_screen = 3
test_computer.my_mouse.right = 2
test_computer.my_mouse.left = 1

res = lib.job(test_computer)
print('Return value: {}.'.format(res))


