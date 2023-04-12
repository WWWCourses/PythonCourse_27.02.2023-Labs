# Dynaminc typing (Python, JavaScript, PHP)
# x = 5
# x = 'abc'
# x = lambda el:el**2
# x = [1,2,3]

# Statics typing (C,C++, C#, Java)
# small int x = 5
# x = '5' error


# -------------------------- Python typing examples -------------------------- #
### Example 1: auto - completion of method
# def print_max_list_number_index(l:list):
# 	max_num = max(l)
# 	print( l.index(max_num) )


# print_max_list_number_index([1,2,3])
# print_max_list_number_index([1,3,2])

# l = [1,2,3]
# print( l.index(3) )

### Example 2
def foo(simb:str,n:int)-> str:
	return simb*n

def bar(x,y):
	print(x*y)

# bar()
print( foo('a',2) )

