from time import sleep
import os

# define our clear function
def clear_screen():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def show_actions(line_width=60):
	print('*'*line_width)

	# print("|{msg:^40s}|".format(msg='Enter a choice'))

	print(f"*{'Enter a choice:':^{line_width-2}s}*")
	print(f"*{'Enter a choice:':<{line_width-2}s}*")
	print(f"*{'Enter a choice:':<{line_width-2}s}*")
	print(f"*{'Enter a choice:':<{line_width-2}s}*")
	print(f"*{'Enter a choice:':<{line_width-2}s}*")
	print('*'*line_width)

	sleep(1)
	clear_screen()





show_actions(30)