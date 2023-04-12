# --------------------------------- Задача 3. -------------------------------- #
# Да се напише програма, която да пита потребителя да въведе едно число от клавиатурата и да покаже съответното число от редицата на Фибoначи. Задачата да се реши с рекурсивна функция.

# 1,1,2,3,5,8, ..
# F(1) = 1
# F(2) = 1
# F(n) = F(n-1) + F(n-2), where n > 2

# Вход: Enter the number 6
# Изход: The 6 th fib term is 8.

def get_user_number()->int:
	while True:
		try:
			x = int(input('Enter a number: '))
			return x
		except:
			print('A NUMBER, please!!!')

def get_fib_element(n:int)->int:
	if n == 1 or n==2:
		return 1
	else:
		return get_fib_element(n-1)+get_fib_element(n-2)


# x = get_user_number()
# 1,1,2,3,5,8, ..
x = 6
print(x)

fib_element = get_fib_element(x)

print(f'The {x} th fib term is {fib_element}.')