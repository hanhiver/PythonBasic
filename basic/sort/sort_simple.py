orig = [1,2,3,-1,5,-3,9,3,-1,9]

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