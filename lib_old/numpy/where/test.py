import numpy as np

a = [0, 0, 1, 2, 4, 5, 7, 8, 7, 4, 0, 2, 1, 0]
b = np.array(a)
print(b)

ind = np.where(b >= (b.max()-1))
print(ind)

center = np.mean(ind)
print(center)


