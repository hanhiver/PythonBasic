# a和b为position-only的参数，
# c和d为既可以positional又可以keyword的参数。
# e和f为keyword-only的参数。
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
