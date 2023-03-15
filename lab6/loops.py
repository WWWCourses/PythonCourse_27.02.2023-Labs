# for el in range(5):
# 	print(el)

# print('END')

# ------------------------------ Nested for loop ----------------------------- #
# # example 1
# for i in 'abc':
# 	for j in range(2):
# 		print(i,j,sep='', end=",")
# 	print('\n')


# --------------------------------- continue --------------------------------- #
# for num in range(5):
# 	if num!=3:
# 		print(num)

# for num in range(5):
# 	if num==3:
# 		continue
# 	print(num)

# # print numbers in [0, 10], without numbers which are divisible by 3
# for i in range(11):
# 	if i%3==0:
# 		continue
# 	print(i)

# ----------------------------------- Break ---------------------------------- #
# for i in range(5):
# 	if i>2:
# 		break

# 	print(i)


# for i in range(3):
# 	for j in range(2):
# 		if i==1:
# 			break

# 	print(j)

# ----------------------------------- pass ----------------------------------- #
# userName = 'Ada'
# if len(userName)>=3:
# 	# TODO: implement logic
# 	pass

# for l in userName:
# 	# TODO: do something
# 	pass

# ----------------------------------- while ---------------------------------- #
# i = 0
# while i!=5:
# 	print(f'Value {i}')
# 	i+=1

# for i in range(5):
# 	print(f'Value {i}')


# TASK: ask user to enter 3digit number
## DO NOT DO THIS
# for i in range(1000000):
# 	x = input('Enter 3digit number: ')
# 	if len(x)==3:
# 		break
# print(f'X = {x}')

### TODO: think of good solution
# x = input('Enter 3 digit number: ')
# while len(x)!=3:
# 	try:
# 		x = input('Enter 3 digit number: ')
# 		int(x)
# 	except:
# 		print('Enter number ONLY')


# try:
# 	x = int(x)
# except:
# 	raise('Not a number')

# # x to be number, 3 dig.
# print(f'X = {x}')


# example 3 (WHILE - DO)

# user_name = input("Enter a name, please: ")
# user_name_length = len(user_name)

# while user_name_length < 3:
#   user_name = input("Enter a name (at least 3 symbols): ")
#   user_name_length = len(user_name)

# print(f"Thank you, {user_name}!")

# example 4 (DO - WHILE)
## ask user to enter a positive number


# do{
# 	x = input('x = ')
# } while(x<=0)

# while True:
# 	x = int(input('x = '))
# 	if x>0:
# 		break

# print(f'x is positive: {x}')

# ## example WHILE - DO
# x = int(input('x = '))
# while x<=0:
# 	x = int(input('x = '))

# print(f'x is positive: {x}')



