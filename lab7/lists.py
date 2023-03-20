# Primary data types: int, float, string, boolean

# List data type
# --------------------------------- Overview --------------------------------- #

# python list (numpy array)

# Maria - 3,
# Ivan - 5,
# Pesho - 4

# student1name = 'Maria'
# student1score = 3

# student_names = ['Maria', 'Ivan', 'Pesho']
# print(student_names)

# RAM
# 	student_names: 0123: [0:0456,1: 0498,2:0428]
# 				   0456: 'Maria'
# 				   0498: 'Ivan'
# 				   0428: 'Pesho'


# l = [1,True, 'a', [4,5,6]]

# print(l)
# print(len(l))


# ---------------------- Access list element (indexing) ---------------------- #

### Read elements:
# l = [1,2,3,4]

# print(l[0])
# print(l[3])

# print(l[3-1]) # 3

# i = 2*1
# print(l[i])

# num = 9
# l1 = [1,2,3]
# l2 = ['a', l1[1], num]

# print(l2) # ['a', 2]


# Nested Lists (LoL: List of Lists)
# m = [
# 	[1,2,3],
# 	[4,5,6],
# 	[7,8,9]
# ]
# print(m)
# print( m[1] ) # [4,5,6]
# print( m[1][1] )  #5
# print( m[2][2] )  #9
#    +[0,1,2,3,4]
#    -[-5,-4,-3,-2,-1]
# l = [1,2,3,4,5]
# print(l[-1])
# print(l[-2])
# print(l[-3])
# print(l[-4])
# print(l[-5])

### Change list element
# l = [1,2,3]
# # RAM:
# # 	l	->	0123: [0231, 0232, 0278]
# # 	l[0]->  0231: 1
# # 	l[1]->  0232: 2
# # 	l[]->  0278: 3

# l[0] = 9
# print(l)

# l = [2, [True, 'Maria'], 'a']
# l[1][1]='Asen'

# print(l) # [2, [True, 'Asen'], 'a']

# l[1] = l[2]
# print(l) # [2, 'a', 'a']

# ------------------------------- identify data ------------------------------ #
# x = '3'
# print(id(x))
# x = '5'
# print(id(x))


# # lists are mutable
# l = [3]
# print(id(l))
# l[0] = 5
# print(id(l))

# --------------------------------- Copy list -------------------------------- #
# data = [1,2,3]

# # make copy of address
# # copy = data

# # make copy of the data
# copy = data[:]

# # change data
# data[0] = 9

# # is copy copy?
# print(copy) #[1,2,3]

# ---------------------------------- Slicing --------------------------------- #
# l[start:end:step]

l = [1,2,3,4,5]

# l2 = l[0:4:1]
# print(l2)# [1,2,3,4]
# l3 = l[:3]
# print(l3)

l4 = l[0:5:2]
# 0-1
# 2-3
# 4-5
print(l4)



