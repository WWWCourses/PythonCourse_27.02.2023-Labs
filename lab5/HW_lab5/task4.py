# Съставете програма, която по въведено трицифренo число проверява дали
# числото се дели на всяка своя цифра. Във въведеното число да няма цифра 0.
# Използвайте проверка на логическо условие - оператор if.
# Пример: 124 Изход: 1:2:4 дели се

### get user input
try:
	x = input('Enter 3 digits number, without 0: ')
	## check if x contains 0:
	# x = 302
	# if x[0] ==0 or x[1]==0 or x[2]==0:
	# 	pass

	if ('0' in x) or (len(x)!=3):
		raise
except:
	print('Your input was wrong')
	exit()


### дали числото се дели на всяка своя цифра.
## get digits from x:
a1 = int(x[0])
a2 = int(x[1])
a3 = int(x[2])
x=int(x)

## check if x is deleted on each digits
if x%a1 == 0 and x%a2 == 0 and x%a3 == 0:
	print(f'{a1}:{a2}:{a3} дели се')
else:
	print('Не се дели!')

# print( 124//4 )
# print( 124%4 )


