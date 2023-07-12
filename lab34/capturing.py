import re

# --------------------------------- Example 1 -------------------------------- #
# Task: match strings which starts and ends with same lower latin letter

# strings = [
#     'alabala', # match
#     'alabal',  # no match
#     '1kk1',    # no match
#     'madam',   # match
#     'bb',   	# match
#     'c 3243 c',   	# match
# ]

# rx = re.compile(r'^([a-z]).*\1$')
# for string in strings:
#     if rx.search(string):
#         print(f'{string} matches')

# --------------------------------- Example 2 -------------------------------- #
# tests = [
#     '12.21', 	# match
#     '34.43', 	# match
#     '123.321',  # no
#     '34.34'		# no
# ]
# rx = re.compile(r'^(\d)(\d)\.\2\1$')

# for test in tests:
#     if rx.search(test):
#         print(f'{test} matches')


# --------------------- Example 3 - named capture groups --------------------- #
# tests = [
#     '12.21', 	# match
#     '34.43', 	# match
#     '123.321',  # no
#     '34.34'		# no
# ]
# #TODO: why throws an error
# rx = re.compile(r'^(?P<first>\d)(?P<second>\d)\.\g<second>\g<first>$')

# for test in tests:
#     if rx.search(test):
#         print(f'{test} matches')

