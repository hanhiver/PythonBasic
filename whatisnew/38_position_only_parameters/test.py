# a和b为position-only的参数，
# c和d为既可以positional又可以keyword的参数。
# e和f为keyword-only的参数。
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

# 以下例子保证函数只能是position-only的参数。
# 通常用来保证和类似的C code一致的调用方式。
def pow(x, y, z=None, /):
    "Emulate the built in pow() function"
    r = x ** y
    return r if z is None else r%z

# 有的时候用来隐藏没啥用的参数keyword。
# 比如标准的len()是如下定义的，避免了len(obj='hello')的影响可读性的调用。
len(obj, /)

# Position-only也使得在未来改变参数名称成为可能。 
# 下面例子未来dist变化了也可以不用修改调用。
def quantiles(dist, /, *, n=4, method='exclusive'):
    pass



