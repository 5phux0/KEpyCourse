import numpy as np
# a. Create a null vector of size 10 but the fifth value which is 1
a = np.empty(10)
a[4] = 1
print('a:', a, '\n')

# b. Create a vector with values ranging from 10 to 49
b = np.arange(10, 50)
print('b:', b, '\n')

# c. Reverse a vector (first element becomes last)
c = b[::-1]
print('c:', c, '\n')

# d. Create a 3x3 matrix with values ranging from 0 to 8
d = np.arange(9).reshape([3, 3])
print('d:', d, '\n')

# e. Find indices of non-zero elements from [1,2,0,0,4,0]
searchVector = np.array([1, 2, 0, 0, 4, 0])
e, = np.where(searchVector != 0)
print('e:', e, '\n')

# f. Create a random vector of size 30 and find the mean value
f = np.random.random(30)
print('f: ', np.mean(f), '\n')

# g. Create a 2d array with 1 on the border and 0 inside
g = np.zeros([10, 10])
g[[0, -1], :] = 1
g[:, [0, -1]] = 1
print('g:\n', g, '\n')

# h. Create a 8x8 matrix and fill it with a checkerboard pattern
rowVec = np.ones([1, 8])
rowVec[:, ::2] = 0
colVec = rowVec.transpose()
h = np.logical_xor(rowVec, colVec)
h = h.view(dtype=np.uint8)
print('h by xor:\n', h, '\n')

# i. Create a checkerboard 8x8 matrix using the tile function
tileMat = np.array([[1, 0], [0, 1]])
h1 = np.tile(tileMat, [4, 4])
print('i by tiling:\n', h1, '\n')

# j. Given a 1D array, negate all elements which are between 3 and 8, in place
j = np.arange(11)
j[3:8] *= -1
print('j: ', j, '\n')

# k. Create a random vector of size 10 and sort it
k = np.random.random(10)
k.sort()
print('k: ', k, '\n')

# l. Consider two random array A anb B, check if they are equal
lA = np.random.randint(0,2,5)
lB = np.random.randint(0,2,5)
np.array_equal(lA, lB)
print('l: {} equals {} is {}\n'.format(lA, lB, np.array_equal(lA, lB)))

# m. How to convert an integer (32 bits) array into a float (32 bits) in place?
m = np.arange(10, dtype=np.int32)
print('m:')
print('Before type conversion:', m.dtype)
mview = m.view(dtype=np.float32)  # This is not a way to do it
m = m.astype(np.float32, copy=False)  # This is my best attempt
print('After type conversion:', m.dtype, '\n')

# n. How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
n = np.dot(A, B)
print('n using ravel and slicing: ', n.ravel()[::4], '\n')
print('n diag: ', np.diag(n))
