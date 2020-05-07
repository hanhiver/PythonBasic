def print_args(*args):
    """args包含了传入所有参数构成的一个列表"""
    print(args)

def print_args2(x, *args):
    """x包含第一个参数，args包含了剩下的所有传入参数组成的列表"""
    print(x)
    print(args)

print_args(1,2,3)
print_args('abc','def','ghi')
print_args('abc',['a','b','c'],1,2,3)

print_args2(1,2,3)
print_args2('abc','def','ghi')
print_args2('abc',['a','b','c'],1,2,3)
