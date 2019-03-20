import numpy as np 

a = np.random.randint(0, 10, (4, 5))
print(a, '\n')

index = np.argsort(a, axis=0)
print(index, '\n')

index_3 = index[..., 3]
print(index_3, '\n')

print(a[index_3])