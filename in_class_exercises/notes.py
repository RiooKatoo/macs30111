import numpy as np


# a = np.arange(6)
# r = a.reshape(2, 3)
# print(r)
# a[0] = 9
# print(r)
# print(r[0, 0])

# print(a[0])
# print(a.sum(axis=0))
# print(a.size)

# x = np.zeros((3, 2, 4))
# print(x)
# x.sum(axis=1).shape

# a = np.arange(10, 16)
# print(a)
# print(a[[0, 2, 5]])

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
j = lst[0:9]
j[0] = 999
print(lst)

zero = np.array([[1, 2, 3], [4, 5, 6]])
print(zero.shape)
print(zero)