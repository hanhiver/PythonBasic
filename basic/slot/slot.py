# 添加__slots__，原先的__dict__就不再存在于这个类了。 
class Nature(object):
    __slots__ = ('tree', 'flower')

print(Nature.__slots__)

# 通过类型可以对slots内部的属性赋值和修改。
Nature.tree = 'liushu'
print(Nature.tree)
Nature.tree = 'songshu'
print(Nature.tree)

# 所有类型实例都共享同一块儿slots空间
a = Nature()
b = Nature()
print(id(a.__slots__))
print(id(b.__slots__))

# 通过实例可以对类型没有赋值的属性进行赋值和修改。
a.flower = 'hehua'
print(a.flower)

# 通过实例赋值和修改的属性属于实例自己。
b.flower = 'shaoyao'
print(a.flower)
print(b.flower)
print(id(a.__slots__))
print(id(b.__slots__))

# 通过实例赋值和修改的slots内容不会被更新到类型。
print(Nature.flower)

# 通过类型对slots内容进行赋值会同步到所有实例，并且实例后续不能再修改。
Nature.flower = 'moli'
print(a.flower)
print(b.flower)
