import ctypes 

so_file = './test.so'
lib = ctypes.cdll.LoadLibrary(so_file)

lib.hello()
lib.hello_cpp()
lib.hello_string()

str1 = ctypes.c_char_p(bytes("dhan", 'utf-8'))
lib.hello_to(str1)
lib.hello_to2(str1)
lib.hello_string_int(str1, 2)

