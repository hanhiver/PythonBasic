import ctypes

so_file = './mt.so'
lib = ctypes.cdll.LoadLibrary(so_file)

lib.testlib()
lib.StartThread(2)

