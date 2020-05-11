from functools import partial

basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int'
print(basetwo('10010'))
