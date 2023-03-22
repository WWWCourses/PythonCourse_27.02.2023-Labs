# --------------------------------- Overview --------------------------------- #
### lists vs dictionaries:
# l = [2,3,4]

# d = {
# 	'a':2,
# 	'b':3,
# 	'c':4
# }

# ----------------------------- Access elements: ----------------------------- #
# user_list = ['maria', 5, 'bulgaria']
# # print(user_list[3])

# user = {
# 	'name':'maria',
# 	'score':5,
# 	'country':'bulgaria'
# }

# print(user['score'])
# print(user.get('score'))


# user = {
# 	'name':'maria',
# 	'scores':[2,3,4],
# 	'country':'bulgaria'
# }

# scores = user['scores']
# # print(scores) # [2,3,4]
# # print(scores[2])

# print( user['scores'][2] )

# user = {
# 	'name':'maria',
# 	'scores':{
# 		'math': 2,
# 		'physics': 3,
# 		'music':4
# 	},
# 	'country':'bulgaria'
# }

# print( user['scores']['music'] )

# ----------------- Task: Get all users who live in "London" ----------------- #
# List of lists
# users:
# 	'Maria', 24, 'Bulgaria, Sofia',
# 	'Asen', 26, 'UK, London'

# users = [
# 	['Maria', 24, ['Bulgaria', 'Sofia']],
# 	['Asen', 26, ['UK', 'London']],
# 	['Ivan', 45, ['UK', 'London']],
# ]

# for user in users:
# 	if user[2][1]=='London':
# 		print(user[0])


# List of dictionaries
# users = [
# 	{
# 		'name': 'Maria',
# 		'age':24,
# 		'address':{
# 			'country': 'Bulgaria',
# 			'town': 'Sofia'
# 		}
# 	},
# 	{
# 		'name': 'Asen',
# 		'age':26,
# 		'address':{
# 			'country': 'UK',
# 			'town': 'London'
# 		}
# 	},
# 	{
# 		'name': 'Ivan',
# 		'age':26,
# 		'address':{
# 			'town': 'London',
# 			'country': 'UK'
# 		}
# 	},
# ]

# for user in users:
# 	if user['address']['town'] == 'London':
# 		print( user['name'] )


# ---------------------------- change/add elements --------------------------- #
# l = []
# l[0] = 1 # Error

# d = {}
# d['a'] = 1 # OK
# print(d)

### change element:
# d = {'a':1, 'b':2}
# d['a'] = 9
# print(d)