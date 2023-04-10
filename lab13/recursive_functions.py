# Рекурсивен акроним
# GNU = GNU is Not Unix


# Рекурсивна функция:
# def foo():
# 	print(1)
# 	foo()

# foo()

def fact(n):
	"""
		n>1=  fact(n) = n × fact(n - 1).
		n=1 fact(n) = 1
	"""
	if n>1:
		return n*fact(n - 1)
	else:
		return 1


print( fact(3) )

# fact(3) = 3*fact(2) = 3*2 = 6
# fact(2) = 2*fact(1) = 2*1 = 2
# fact(1) = 1