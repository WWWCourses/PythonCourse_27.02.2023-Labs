# ----------------------------- input into tuple ----------------------------- #
# data = input('Enter data: ')
# t = tuple(input('Enter data: '))

# print(data)
# print(t)


# ------------------------ create tuple from 1 element ----------------------- #
# l = [1]
# s = {1}
# t1 =(1) # THIS IS NOT A TUPLE!!!
# t = (1,)

# print(t)

# --------------------------- indexing and slicing --------------------------- #
# t = tuple(range(1,11))
# print(t)
# # print( t[::-1] )
# print( t[::2] )


# ------------------------ Data structures with tuples ----------------------- #
# id| userName | age
# 1 | Maria    | 23
# 2 | Asen     | 31
# 3 | Pesho    | 19

# Find the name of younger user:

#### Solution with List of Dictionaries
# ages = [23,31,19]
# min = ages[0]

# for age in ages:
# 	if age<min:
# 		min=age
# print(min)

# users = [
# 	{
# 		'name': 'Maria',
# 		'age':23,
# 		'id': 1
# 	},
# 	{
# 		'name': 'Sasho',
# 		'age':16,
# 		'id': 4
# 	},
# 	{
# 		'name': 'Asen',
# 		'age':31,
# 		'id': 2
# 	},
# 	{
# 		'name': 'Pesho',
# 		'age':19,
# 		'id': 3
# 	}
# ]

# min = users[0]['age']
# min_user = users[0]

# for user in users:
# 	age = user['age']
# 	if age<min:
# 		min=age
# 		min_user = user

# print(min_user['name'])



### Solutions witj List of Tuples
# id| userName | age
# 1 | Maria    | 23
# 2 | Asen     | 31
# 3 | Pesho    | 19


# users_data = {
# 	'age': 		(32, 		31,		19),
# 	'names': 	('Maria','Asen','Pesho')
# }

# min_age = min( users_data['age'] )
# min_index = users_data['age'].index(min_age)

# print(users_data['names'][min_index])

# --------------------------------- frozenset -------------------------------- #

sentence = 'orange banana orange banana cherry'
words = sentence.split(' ')
print(words)
words_unique = frozenset(words)
print(words_unique)


