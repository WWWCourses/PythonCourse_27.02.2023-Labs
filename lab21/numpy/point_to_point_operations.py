import numpy as np

######## Operations are Element-wise (point-to-point) !!!!!
# l1 = [1,2,3]
# print( l1 + 3 )

# a=np.arange(1,4)
# print(a)
# print(a.shape)
# print(a*3)
# print(a/3)
# print(a+3)
# print(a-3)

# a2=np.arange(4,7)
# print(a2)
# print(a2.shape)



# print('='*30)
# print(a+a2)
# print(a-a2)
# print(a/a2)
# print(a*a2)


# -------------------------------- Comparison -------------------------------- #

# a=np.array([1,-2,3,-4,5])
# # print(a<2)

# a_new = np.where(a>=0,1,0)
# print(a_new)


# a=np.array([1,-2,3,-3,5])
# a_new = np.select([a>=0,a%2==0],[1, 9], default=888)
# print(a_new)


# ---------------------------- Logical Operations ---------------------------- #
# a1 = np.array([1,2,3])
# a2 = np.array([4,5,6])

# a1_bool = a1%2==0
# a2_bool = a2%2==0
# print(a1_bool)
# print(a2_bool)

# print( np.logical_and(a1_bool, a2_bool)) # [F, F,FB]
# print( np.logical_or(a1_bool, a2_bool)) # [F, F,FB]



# ---------------------------------- Masking --------------------------------- #
# a1 = np.array([1,2,3])
# mask = [True, False, True]

# a_new =a1[mask]
# print(a_new)


# print(a1%2==0)
# a_evens = a1[ a1%2==0 ]
# print(a_evens)

