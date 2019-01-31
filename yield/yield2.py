a = [1, 2, 3]
static s = 0

def gen():
    for i in a:
        #print(i)
        yield i


print(*gen())
print(*gen())



