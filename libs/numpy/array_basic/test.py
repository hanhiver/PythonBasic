import numpy as np

a = np.arange(10)
print(a)

b = a.reshape((2,5))
print(b)

print(b[b>0].min())

print(b[b>b.min()])

for i in np.nditer(b):
    print(i)

for i in np.nditer(b, op_flags = ['readwrite']):
    i[...] = 2 * i

print(b)

print(a.ptp())

d = {'a':a, 'b':None}

print(d['a'])

print(d['a'][d['a']>4])

    
