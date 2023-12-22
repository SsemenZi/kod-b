import numpy as np
arr1 = np.random.randint(1, 10, size=100)
print((len(arr1[arr1 > 7] / len(arr1) * 100)))
#nomer 2
count = 0
b = 20
for i in range(1000):
    arr1 = np.random.randint(1, 10, size=100)
    len(arr1[arr1 > 7] / len(arr1) * 100)
    if len(arr1[arr1 > 7] / len(arr1) * 100) == b:
        count += 1
print(count / 1000)
#nomer 3
n = np.full((10, 10), range(1, 11))
print(n)
#nomer 4
n = np.full((10, 10), range(1, 11))
sum = n.sum(axis=0)
print(sum)