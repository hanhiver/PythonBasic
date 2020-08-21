orig = [1,2,3,-1,5,-3,9,3,-1,9]
strings = ['a3a', 'x1x', 'd2d', '141', 'p0p', 'o0o']

def cmp(a):
    if a > 0:
        return True
    else:
        return False

a = orig.copy()      
print(a)
a.sort()
print(a)

a = orig.copy()
print(a)
a.sort(key=cmp)
print(a)

a = strings.copy()
print(a)
a.sort()
print(a)

def cmp2(item):
    second = item[1]
    second = int(second)
    if second > 2:
        return True
    else:
        return False

a = strings.copy()
print(a)
a.sort(key=cmp2)
print(a)