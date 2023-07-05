import re

# Task1: Valid pin: 4 digits
user_pins = '23456'
rx = re.compile(r'\d{4}')

if rx.search(user_pins):
    print('Valid')
else:
    print('Invalid')
