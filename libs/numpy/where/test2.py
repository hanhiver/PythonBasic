import numpy as np

np.set_printoptions(precision=1, suppress=True)

a = [0, 0, 1, 2, 4, 5, 7, 8, 7, 4, 0, 2, 1, 0]
b = np.array(a)
print('b   :', b)

srt = b.argsort(kind='stable')
print('SRT: ', srt)

idx = srt[-3:]
print('IDX: ', idx)

bmax = b[idx]
print('BMAX: ', bmax)

center = np.median(bmax)
print('Center: ', center)


