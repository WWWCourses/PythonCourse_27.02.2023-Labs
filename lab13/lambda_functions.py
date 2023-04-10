# def power(a,b):
# 	return a**b


# bar = power
# print( power(2,3) )
# print( bar(2,4) )

# ----------------------- Function as function argument ---------------------- #
# def caller(f,x,y):
# 	# f = add
# 	print('Caller is calling f: ')
# 	f(x,y)

# def add(x,y):
# 	print(x+y)

# # bar = add
# # bar(2,3)

# caller( add,5,6 )

# ----------------------------- lambda functions ----------------------------- #
# def foo(x,y):
# 	return x+y

# foo_lambda = lambda x,y:x+y

# print( foo(2,3) )
# print( foo_lambda(2,3) )


### example 1
# def power(a,b):
# 	return a**b

# power = lambda a,b:a**b
# res = power(2,3)
# print(res)


# def calulator(x,y, f):
# 	print( f(x,y) )


# def add(x,y):
# 	return x+y;

# calulator(2,3,f=add)


# calulator( lambda x,y:x+y, 2,3 )
# calulator( lambda x,y:x-y, 2,3 )
# calulator( lambda x,y:x*y, 2,3 )
# calulator( lambda x,y:x/y, 2,3 )



# ------------------ Sort list of tupples by second element ------------------ #
l = [
	(1,2),
	(2,1),
	(1,3)
]

# def sort_by_tupple_key(t):
# 	print(t[1])
# 	return t[1]

# l_sorted = sorted(l, key=sort_by_tupple_key )

# l_sorted = sorted(l, key= lambda t:t[1])
# print(l_sorted)

