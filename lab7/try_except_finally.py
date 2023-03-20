try:
	# block which can raise error
	x = int(input('Number: '))
except:
	# if there is error
	print('Except Block')
finally:
	# alwayes executed
	print('Finaly Block')

print('End')