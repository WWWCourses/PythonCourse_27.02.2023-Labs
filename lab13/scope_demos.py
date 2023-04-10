# ------------------------------ Scope Examples ------------------------------ #
# def foo():
# 	x = 2
# 	def bar():
# 		x = 3
# 		print(f'x in bar: {x}')

# 	print(f'x in foo: {x}')
# 	bar()

# x = 1

# foo()
# print(f'x in global: {x}')


# output:
# x in foo: 2
# x in bar: 3
# x in global:1

# foo = {
#    'x': 2
#    'bar': [function]
# }
# #

# Global={
# 	'foo': [function],
# 	'x': 1,
#   '__name__': '__main__',
#    ...
# }



# --------------------- Print global and local namespace --------------------- #
# from pprint import pprint

# def foo():
# 	# TODO: how to print locals before locals definitions
# 	x = 3
# 	pprint( locals() )

# x = 1

# pprint( globals() )
# foo()
# print(x)

# --------------------------------- Example 1 -------------------------------- #
# number = 5

# def foo(number):
# 	# number = 5
# 	# print(number)
# 	# number=3

# 	number+=1
# 	# number=number+1
# 	print(number)


# foo(number)
# print(f'number in global: {number}')


# --------------------------------- Example 2 -------------------------------- #
# def inc(counter):
# 	counter+=1
# 	return counter
# 	# print(counter)

# counter = 1

# counter = inc(counter)
# counter = inc(counter)
# counter = inc(counter)
# counter = inc(counter)
# counter = inc(counter)

# print(counter)


# -------------------- Mutable data as function arguments -------------------- #
# def bar(x):
# 	x = 10

# def foo(l):
# 	# l = global.l
# 	l[1] = 10


# x = 5
# bar(x)
# print(x) # 5

# l = [1,2,3]
# foo(l)
# print(l) # [1,10,3]