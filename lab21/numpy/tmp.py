import numpy as np


# --------------------------------- resize() --------------------------------- #
# a = np.arange(5,11)
# print(a)
# a_new = np.resize(a, (2,4))
# a.resize((2,4))
# print(a_new)
# print(a)


# --------------------------------- reshape()--------------------------------- #
# a = np.arange(5,11)
# # a_new = np.reshape(a_new, (2,3))
# a_new = a.reshape((2,3))
# print(a_new)

# -------------------------------- linspace() -------------------------------- #
# a_lin = np.linspace(1,10,num=3)
# print(a_lin)

# # 1, 2, 3, 4, 5 ,6, 7, 8, 9
# # 1 5 9

# a_log = np.logspace(1,10,num=3)
# print(a_log)

# ------------------------------ create 2d array ----------------------------- #
# # m1 = np.zeros((2,3),dtype=np.int8)
# # m1 = np.ones((2,3),dtype=np.int8)
# m1 = np.full((2,3),9,dtype=np.int8)
# print(m1)


# ------------------------------- Stat methods ------------------------------- #

# a = np.array([1,3,5,5], dtype=np.int8)
# print(a)
# print(np.average(a))
# print(np.mean(a))
# print(np.median(a))
