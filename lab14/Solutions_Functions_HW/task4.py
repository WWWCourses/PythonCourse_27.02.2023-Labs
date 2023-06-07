# --------------------------------- Задача 4. -------------------------------- #
# Да се напише програма, която да пита потребителя да въведе число от клавиатурата и да пресметне факториелът на това число. Да се използва рекурсия.

# n! = n*(n-1)!
# 0! = 1

# Вход: Enter the number 5
# Изход: Factorial of 5 is 120


# from lib.auxiliary import get_user_number
import lib.auxiliary as auxiliary

x = auxiliary.get_user_number()

def fact(n)->int:
	if n==0:
		return 1
	else:
		return n*fact(n-1)


print(f'Factorial of {x} is {fact(x)}')
