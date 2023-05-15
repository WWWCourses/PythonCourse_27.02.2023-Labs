import numpy as np
# l = [1,2,3,4,5]
# l1 = [1,2,3]
# l2 = [4,5,6]
# ll = [l1,l2]
# # create array from python list
# arr = np.array([1,2,3,4,5])
# arr2dim = np.array([l1,l2])


# print(ll)
# print(arr2dim.dtype)



# arr = np.array( range(11) )
# arr = np.arange(11,dtype=np.ushort)
# arr_str = np.array(['a','b','c'])

# print(arr_str.dtype)
# print(arr.dtype)


# arr1d = np.arange(1,7)
# arr2d = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# print(arr1d.shape)
# print(arr2d.shape)

# print(arr1d.ndim)
# print(arr2d.ndim)

arr1d = np.arange(1,7) # [1,2,3,4,5,6]
# arr2d = np.reshape(arr1d, (3,2,1))
arr2d = arr1d.reshape((3,2,1))
print(arr1d)
print(arr2d)

