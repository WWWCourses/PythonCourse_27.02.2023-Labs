# -------------------------------- The Bsisics ------------------------------- #
# user_name = 'Ada'

# print(f'~'*30)
# print(f'Hello, {user_name}')
# print(f'~'*30)

# user_name = 'Pesho'
# print(f'~'*30)
# print(f'Hello, {user_name}')
# print(f'~'*30)


# def print_hello(user_name, user_surname):
# 	print(f'~'*30)
# 	print(f'Hello, {user_name} {user_surname}')
# 	print(f'~'*30)


# print_hello('Ada', 'Byron')
# print_hello('Pesho', 'Peshev')

# RAM:
# 	print_hello: 0x32432: <function>
# 	user_name: 04583543: 'Pesho'

# def foo(l):
# 	# l = [1,2,3]
# 	print(l)

# l = [1,2,3]

# # foo( l )
# # foo( [2,3] )
# foo( 2,3 )
# print('END')

# # RAM:
# GLOBAL:
# 	foo: 0x123: <function>
# 	  l: 0x343: [1,2,3]
#


# ---------------------------- Default Parameters ---------------------------- #
# def print_hello(user_surname, user_name='', age=100):
# 	print(f'~'*30)
# 	print(f'Hello, {user_name}{user_surname}. You are {age} old!')
# 	print(f'~'*30)

# print_hello('Pesho', 'Peshev', 'MiddlePeshev')
# print_hello('Pesho', 'Peshev')
# print_hello( 'Peshev')

# ----------------------------- Keyword Argument ----------------------------- #
# def print_hello(user_surname, age, user_name=''):
# 	print(f'~'*30)
# 	print(f'Hello, {user_name}{user_surname}. You are {age} old!')
# 	print(f'~'*30)

# print_hello(age=23, user_name='Pesho', user_surname='Pechev')
# print_hello('Peshev',age=23,'Pesho')

# ----------------------------------- *args ---------------------------------- #
# def add(*args):
# 	args_sum = sum(args)
# 	print(f'Sum = {args_sum}')

# add(2,3)
# add(4,5)
# add(1,2,3)
# add(1,2,3,4)

# # t = (1,2,3)
# # print(f'sum = {sum(t)}')


# def foo(x,y, *args):
# 	# x = 1, y = 2, args = (3,4)
# 	print(x, y, args)

# foo(1,2)
# foo(1,2,3,4)

# --------------------------------- **kwargs --------------------------------- #
# def foo(**kwargs):
# 	print(kwargs)

# foo(x=1, y=2)
# foo(x=1, y=2, z=3)


# ----------------------- Example of *args && **kwargs ----------------------- #
# def foo(*args,**kwargs):
# 	print(args)
# 	print(kwargs)

# # foo(1,2, user='Pesho', color='red')
# # foo(1,2,3, user='Pesho')
# foo(user='Pesho')

# -------------------------- Functions in dictionary ------------------------- #
# def foo():
# 	print('Foo')

# my_functions = {
# 	'x': 1,
# 	'foo': foo,
# }

# my_functions['x']+2
# my_functions['foo']()

# ---------------------------- Unpacking arguments --------------------------- #
# def greet_user(user_name, age):
# 	print(user_name, age)

# data = ['Pesho', 23]

# # greet_user(data[0],data[1])
# greet_user( *data )


# def greet_user(user_name, age):
# 	print(user_name, age)

# data = {
# 	'user_name':'Pesho',
# 	'age':23
# }

# greet_user(data['user_name'], data['age'])
# greet_user(**data)
# greet_user(user='Pesho', 'age'=23)


# --------------------------- Function Return Value -------------------------- #

# y = add(2,3)
# add(2,3) + add(3,4)
# def add(x,y):
# 	return x+y

# res = add(2,3) + add(3,4)
# print(res)

def foo(x,y):
	if(x%2==0 and y%2==0 ):
		return x+y
	else:
		return

	print('foo')


print( foo(6,4) )











