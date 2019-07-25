import ctypes

mylib = ctypes.cdll.LoadLibrary("./libtest.so")
print("Lib loaded.")

mylib.testlib()

mylib.check_value()
mylib.check_value()

mylib.init_pointer()
mylib.check_pointer()
mylib.check_pointer()

mylib.init_class()
mylib.call_class()
mylib.call_class()
mylib.delete_class()

