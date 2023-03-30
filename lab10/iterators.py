# ----------------------------------- Notes ---------------------------------- #
# iterable - everythin, which can be iter()

# iterator -


# --------------------------------- Iterator --------------------------------- #
# for l in 'abc':
# 	print(l)

# iterator = iter('abc')
# el1 = next(iterator)
# el2 = next(iterator)
# el3 = next(iterator)
# # el4 = next(iterator)

# print(el1, el2, el3)

# l = [1,2,3]
# print(dir(l))
# iterator = iter(l)
# iterator = l.__iter__()


# print( next(iterator) )

# -------------------------- Iterate over dictionary ------------------------- #
# d = {'a':1, 'b':2}

# for key in d:
# # for key in d.keys():
# 	print(key)

# for el in d.values():
# 	print(el)

# print( d.items() )
# for key, value in d.items():
# 	print(f'{key}-{value}')


# ----------------------------- Iterable Examples ---------------------------- #


# for el in range(1,4):
# 	print(el)

# for el in [1,2,3]:
# 	print(el)

# r1 = range(1, 1000)
# r2 = range(1, 1_000_000)



# ---------------------------- Fibonachi Iterable ---------------------------- #
# 0,1,1,2,3,5,8,13..
# class Fib:
# 	def __init__(self,end) -> None:
# 		self.first = 0
# 		self.second = 1
# 		self.end = end

# 	def __iter__(self):
# 		return self

# 	def __next__(self):
# 		value = self.second
# 		self.second +=self.first
# 		self.first = value
# 		if value<self.end:
# 			return value
# 		else:
# 			# print('iterator end')
# 			exit()


# fib = Fib(50)
# # fib_iter = iter(fib)
# # print( next(fib_iter) )
# # print( next(fib_iter) )
# # print( next(fib_iter) )
# # print( next(fib_iter) )
# # print( next(fib_iter) )

# for el in fib:
# 	print(el)


# Fibonachi Generator
def fib(end):
	first, second = 0,1
	while True:
		if second<=end:
			yield second
			first, second = second, first+second
		else:
			break



for el in fib(50):
	print(el)

