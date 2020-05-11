import ctypes

mylib = ctypes.cdll.LoadLibrary("cpptest.so")

class sub_struct(ctypes.Structure):
    _fields_ = [
        ("test_char_p",ctypes.c_char_p),
        ("test_int",ctypes.c_int)]

class struct_def(ctypes.Structure):
    _fields_ = [
        ("stru_string",ctypes.c_char_p),
        ("stru_int", ctypes.c_int),
        ("stru_arr_num", ctypes.c_char*4),
        ("son_struct", sub_struct)]

struct_mystruct = struct_def()
struct_mystruct.stru_string = b"string in the struct"
struct_mystruct.stru_int = 99
struct_mystruct.stru_arr_num = b"ABCD"
struct_mystruct.son_struct.test_char_p =b"sub struct of the string"
struct_mystruct.son_struct.test_int = 10
mylib.test(struct_mystruct, ctypes.byref(struct_mystruct))

