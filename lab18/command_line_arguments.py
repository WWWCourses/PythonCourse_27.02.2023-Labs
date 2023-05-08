import sys
import os

print( os.getcwd() )
print( sys.argv )

['lab18/command_line_arguments.py', 'iva', '18']

# user_name = sys.argv[1]
# user_age =  sys.argv[2]
(user_name, user_age) = sys.argv[1:]

print(f'Hello, {user_name}. You are {user_age} years old')