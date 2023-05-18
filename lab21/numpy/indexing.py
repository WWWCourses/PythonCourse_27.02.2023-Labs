import numpy as np


# l = [1,2,3,4,5,6,7,8,9,10]
# print(l[0][0])

# -------------------------------- Indexing 1D ------------------------------- #
# a = np.arange(1,11)
# print(a[-1])
# print(a[1])

# -------------------------------- INdexing 2D ------------------------------- #
# a2d = a.reshape((2,5))
# print(a2d)

# print(a2d[1][2]) # => VERY BAD
# print(a2d[1,2])    # => THE WRIGHT WAY

# -------------------------------- Indexing 3D ------------------------------- #
# a = np.arange(1,13)

# a3d = a.reshape((1, 4, 3))
# print(a3d)
# print('*'*30)
# print(a3d[0,2,1])




# -------------------------------- Slicing 1D -------------------------------- #
# l = [1,2,3,4,5,6,7,8,9,10]
# l_new = l[-1::-1]
# print(l_new)

# a = np.arange(1,11)
# print(a)
# a_new = a[-1::-1]
# print(a_new)

# -------------------------------- Slicing 2D -------------------------------- #
# a = np.arange(1,11)
# a2d = a.reshape((2,5))
# print(a2d)

# a_new  = a2d[:,0:2]
# a_new  = a2d[:,-1]
# a_new  = a2d[:,[0,-1]]


# print('='*30)
# print(a_new)

# [[1,6], [5,10]]