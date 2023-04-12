# --------------------------------- Задача 1. -------------------------------- #
# Да се напише функция, която да търси в списък. Като параметър да приема
# списък и да принтира ако елементът е в списъка неговата позиция, ако ли не да
# принтира, че не е намерен.

# Вход: [1, 2, 5, 9, 10], 5
# Вход: [1, 2, 5, 9, 10], 3
# Изход: Position 2
# Изход: Not found

# def find_in_list(l:list, element:any):
# 	'''Implement using list.index() method'''

# 	if element in l:
# 		idx = l.index(element)
# 		print(f'Position {idx}')
# 	else:
# 		print('Not found')

# find_in_list([1, 2, 5, 9, 10], 5)
# find_in_list([1, 2, 5, 9, 10], 3)


# --------------------------------- Задача 2. -------------------------------- #
# Да се промени горната задача така, че тя да връща стойност и след това да се
# принтира резултатът в зависимост от върната стойност от функцията. Да се напише и още една функция, която да принтира резултатът от търсенето.
# Вход: [1, 2, 5, 9, 10], 5
# Вход: [1, 2, 5, 9, 10], 3
# Изход: Position 2
# Изход: Not found


def find_in_list(l:list, element:any):
	'''Implement using list.index() method'''

	if element in l:
		idx = l.index(element)
	else:
		idx = -1

	return idx

def print_result(idx):
	if idx>=0:
		print(f'Position {idx}')
	else:
		print('Not found')

def print_index(l:list, element:any):
	idx = find_in_list(l,element)
	if idx>=0:
		print(f'Position {idx}')
	else:
		print(f'Not found')

# idx = find_in_list([1, 2, 5, 9, 10], 5)
# print_result(idx)

# idx = find_in_list([1, 2, 5, 9, 10], 3)
# print_result(idx)

# print_index([1, 2, 5, 9, 10], 5)
# print_index([1, 2, 5, 9, 10], 3)