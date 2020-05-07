from functools import reduce 

def func(x, y):
    print("X: ", x, ", Y: ", y)
    return x + y

a = [1, 2, 3, 4]
c = reduce(func, a)
print("C: ", c)