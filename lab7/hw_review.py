# Задача 3. Да се напише програма, която да създаде следният шаблон:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# middle_count = 5

# top_rows_count = middle_count -1
# bottom_rows_count = top_rows_count

# for i in range(1, top_rows_count+1):
# 	print('*'*i)

# print('*'*middle_count)

# for i in range(bottom_rows_count, 0, -1):
# 	print('*'*i)

# Задача 4. Да се напише програма, която да обръща буквите на дадена дума на обратно.
# Думата да бъде въведена от клавиатурата. Като за целта използвате цикъл.
# Вход:
# Input a word to reverse: Hello
# Изход:
# olleH

# word = 'test'

# for i in range(len(word)-1, -1, -1):
# 	print(word[i], end='')


# Задача 10. Да се състави програма, която изчислява сумата на произведенията от 1 до  въведено едноцифрено число.

# Сумата се формира така:
# 1*2 + 2*3*4 +..+n*(n+1)*(n+2)*..*2*n

# 1*2 = 			2
# 2*3*4 = 			24
# 3*4*5*6 =			360
# 4*5*6*7*8 =       6720

# Вход: 4
# Изход: 7106

# n = 4
# sum = 0
# for i in range(1,n+1):
# 	product = 1

# 	# j = i
# 	# while j!= 2*i+1:
# 	# 	product*=j  	# product = product * j
# 	# 	j+=1

# 	for j in range(i,2*i+1):
# 		product*=j

# 	sum+=product

# print(f'sum={sum}')


# Задача 14. Да се напише програма, която да генерира число на случен принцип и да подкани потребителя да познае това число.
# Да извежда следните стойности too low, too high, или exactly right, в случай, че потребителя е познал, или не числото.

# 1..10 => 5

# > 3 => too low
# > 7 => too high
# > 5 => exactly right

import random

start = 1
end = 10

### generate machine number:
machine_number = random.randint(start, end)
print(machine_number)


# ### game logic:
# while True:
# 	### get valid user number:
# 	while True:
# 		while True:
# 			try:
# 				user_number = int(input(f'Guess my number [{start}..{end}] '))
# 				break
# 			except:
# 				print('You must ener a number!!!')

# 		# if user_number>=start and user_number<=end
# 		if start<=user_number<=end:
# 			break

# 	if user_number<machine_number:
# 		print('too low')
# 	elif user_number>machine_number:
# 		print('too high')
# 	else:
# 		print('exactly right')
# 		break