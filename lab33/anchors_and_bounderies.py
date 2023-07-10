import re

# --------------------------------- Example 1 -------------------------------- #
# test = """a b"""
# rx = re.compile(r'^a\sb$')

# if rx.search(test):
#     print('Match')
# else:
#     print('No match')


# --------------------------------- Example 2 -------------------------------- #
# valid password: at least 8 symbols, which are latin letters and number
# user_passes = [
#     '12345678', # valid
#     '1234567abadhjshdjsdhjdshjdshfjdsh', # valid
#     '1234 5678', # invalid
#     '1234567', # invalid
#     '*****12345678', # invalid
#     '12345678*', # invalid
# ]

# rx = re.compile(r'^[a-z0-9]{8,}$')

# for user_pass in user_passes:
# 	if rx.search(user_pass):
# 		print(f'{user_pass} is valid')
# 	else:
# 		print(f'{user_pass} is invalid')


# --------------------------------- Example 3 -------------------------------- #
# # How match are the lines which starts with digit?
# test = """
# 1kfddskkfds
# 2kfdllkfdldf
# jdfkds5kflds
# 2kdslfkds
# 4lkdslkfds"""

# rx = re.compile(r'^\d', re.M)

# res = rx.findall(test)
# print(len(res))

# --------------------------------- Example 4 -------------------------------- #
# How match are the lines which contains only digits?
# test = """
# # 124332432432
# # 234,
# # 98584935
# # _123

# # 8943985"""

# rx = re.compile(r'^\d+$', re.M)

# res = rx.findall(test)
# print(len(res))

# --------------------------- Word boundaries (\b) --------------------------- #
# \b = XY or YX
# X = \w == [A-Za-z0-9_]
# Y = \W == [^A-Za-z0-9_] and ^ and $

# '!'   = \b -> 0
# 'a'   = \b -> 2
# 'ab'  = \b -> 2
# 'a_b'  = \b -> 2
# 'a!'   = \b => 2

# TASK: replace all occurences of word 'the' with '@'
# text = """
# Matchesthe  beginning of the string (or the line, if m flag is used)
# $	Matches the end of,the string (or there line, if m flag is used)
# \b	Matches on word boundaries, i.e. between word(\w) and non-word(\W) characters.
# Note that the start and end of string are considered as non-word characters.
# \Z	Matches only at the end of the string.
# """

# rx = re.compile(r'\bthe\b')
# replaced = rx.sub('@',text)

# print(text)
# print('*'*30)
# print(replaced)

# --------------------------------- Example 5 -------------------------------- #
import re

strings = [
  '', 	# 0
  'a',  # 2
  '@',  # 0
  '@a', # 2
  'aa', # 2
  'a!', # 2
  'a,a',# 4
]
rx = re.compile(r'\b');

for string in strings:
  res = rx.findall(string)
  print("{} word bounders counted in {}".format(len(res), string))