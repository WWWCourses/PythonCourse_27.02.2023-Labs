import os

def write_user_name(file_path):
    user_name = input('Enter name: ')
    f = open(file_path, 'a')
    f.write(f'{user_name}\n')



def get_user_names(file_path):
	f = open(file_path)
	user_names = f.readlines()

	user_names = [el.rstrip() for el in user_names]
	print(user_names)

	f.close()
	return user_names



# write_user_name('users.txt')
# write_user_name('users.txt')
user_names = get_user_names('users.txt')
# for user in user_names:
#       print(user)


