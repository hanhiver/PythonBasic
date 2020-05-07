# map(func, seq)，就是对Seq中所有的元素从左到右取出来，
# 然后应用func函数，并将函数的返回值存储到列表里。 
# 需要注意的是，map返回的是一个迭代器，还需要一个额外的步骤取出所有内容。 
a = [1, 2, 3]
b = [4, 5, 6]

def add(x):
    return x+1

c = list(map(add, a))
print(c)

# 将两个数组对应单元的值加起来。
d = list(map(lambda x, y: x + y, a, b))
print(d)