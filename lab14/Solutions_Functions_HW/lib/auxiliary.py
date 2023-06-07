def get_user_number()->int:
	while True:
		try:
			x = int(input('Enter a number: '))
			return x
		except:
			print('A NUMBER, please!!!')

def get_user_name():
	pass