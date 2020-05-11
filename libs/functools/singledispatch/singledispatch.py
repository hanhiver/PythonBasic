# 根据不同类型重载函数。
from functools import singledispatch
from decimal import Decimal

# 定义函数的时候使用singledispatch修饰符。
@singledispatch
def func(arg, verbose=False):
    if verbose:
        print("Let me just say, ", end=" ")
    print(arg)

# 对于不同类型的重载，使用register进行注册。 
@func.register
def _(arg: int, verbose=False):
    if verbose: 
        print("Strength in numbers, eh? ", end=" ")
    print(arg)

@func.register
def _(arg: list, verbose=False):
    if verbose: 
        print("Enumerate this: ")
    
    for i, elem in enumerate(arg):
        print(i, elem)

# 也可以将类型放在register部分进行注册。 
@func.register(complex)
def _(arg, verbose=False):
    if verbose: 
        print("Better than complicated. ", end=" ")
    print(arg.real, arg.imag)

# 通过register后注册。
def nothing(arg, verbose=False):
    print("Nothing.")
func.register(type(None), nothing)

# 可以对不同类型一起注册同一个函数
@func.register(float)
@func.register(Decimal)
def fun_num(arg, verbose=False):
    if verbose:
        print("Half of your number: ", end=" ")
    print(arg/2)
print(fun_num is func)

func("Hello, world")
func("test.", verbose=True)
func(42, verbose=True)
func(['spam', 'spam', 'eggs', 'spam'], verbose=True)
func(None)
func(1.23)
print(func.registry.keys())
