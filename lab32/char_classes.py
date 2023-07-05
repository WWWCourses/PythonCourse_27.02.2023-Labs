import re

# character sets 	: [0-9]
# character classes : \d

# ------------------------------------ dot ----------------------------------- #
# test = '''1
# 1'''
# print(test)
# rx = re.compile(r'1.1')

# if rx.search(test):
#     print('match')


# ---------------------------- \w (word character) --------------------------- #
# # '\w' = '[A-Za-z0-9-]'
# # task: print all words - word is a more than 3 symbols sequence of letters, digits and '-'
# test = 'Character classes, can be regarded as r2d3 shorthands for some of the most used character sets state-of-the-art.'

# rx = re.compile(r'\w{3,}')

# for word in rx.findall(test):
#     print(word)


# ---------------------------- \s = any witespace ---------------------------- #
#'\s' = ' [ \t\n\r\f\v]'

test = '''Line 1
Line 2
Line 3'''

# rx  = re.compile(r'\n')
# rx  = re.compile(r'\n\r')
rx  = re.compile(r'\n\r?')
print(len(rx.split(test)))








