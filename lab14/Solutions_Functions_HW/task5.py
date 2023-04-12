# --------------------------------- Задача 5. -------------------------------- #
# Да се създаде програма, която да реализира няколко функции: добавяне (Add),
# изтриване (Remove), изтриване на всичко (clear), показване (show), край на програмата (Quit). Програмата да реализира програмна логика за количка за пазаруване (като тези в онлайн магазините). Потребителят да въвежда от клавиатурата даден елемент, след което да има възможност да го добави, изтрие, да види какво е поръчал.


import os
from time import sleep

# define our clear function
def clear_screen():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def add(products:list, cart:list):
	list_cart_items(cart)
	print(f'Add product to cart:')
	show_products(products)

	choice = int(input(f'Enter product number [1-{len(products)}]: '))
	product = products[choice-1]
	cart.append(product)

	print_status(f'{product} was added to your cart!')

def remove(cart:list):
	print(f'Remove product from cart:')
	show(cart)

	choice = int(input(f'Enter product number [1-{len(cart)}]: '))
	product = cart.pop(choice-1)

	print_status(f'{product} was removed from your cart!')

def clear(cart:list):
	cart.clear()
	print_status(f'Your casrd is clear!')

def show(cart):
	print(f'Items in cart:')
	for idx in range(len(cart)):
		print(f'\t{idx+1}. {products[idx]}')
	sleep(3)

def quit():
	print('Good bye!')
	exit()

def show_actions(line_width=60):
	print('*'*line_width)
	# [[fill]align][sign][#][0][minimumwidth][.precision][type]
	# print('{:^24s}'.format("MyString"))
	print(f'* {"Select an action":^{line_width-4}s} *')
	print(f'* {"1. Add":<{line_width-4}s} *')
	print(f'* {"2. Remove":<{line_width-4}s} *')
	print(f'* {"3. Clear":<{line_width-4}s} *')
	print(f'* {"4. Show":<{line_width-4}s} *')
	print(f'* {"5. Quit":<{line_width-4}s} *')
	print('*'*line_width)

def print_status(stat_msg='', line_width=60, ):
	print('*'*line_width)
	print(f'* {stat_msg:^{line_width-4}s} *')
	print('*'*line_width)

def show_products(products):
	# print(f'Available products: ')
	for idx in range(len(products)):
		print(f'\t{idx+1}. {products[idx]}')

def list_cart_items(cart):
	print(f'Cart: {cart}\n')
	# print(f'\nCart: ', end='')
	# for item in cart:
	# 	print(f'{item}', end='; ')
	# print('\n\n')


LINE_WIDTH = 40
products = ['Bread', 'Beer', 'Watter', 'Rise', 'Sugar']
cart = []

while True:
	list_cart_items(cart)
	show_actions()
	choice = input(f'Enter your choice [1-5]: ')
	print()
	clear_screen()

	if 	 choice=='1': add(products, cart)
	elif choice=='2': remove(cart)
	elif choice=='3': clear(cart)
	elif choice=='4': show(cart)
	else:
		quit()

	sleep(1)
	clear_screen()
