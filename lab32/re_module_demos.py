import re

# ------------------------------ compiled regex ------------------------------ #
# test = 'abc12356'
# rx_str = r'[7-9]{3}'
# print(type(rx_str))

# # rx=re.compile(rx_str)
# print(type(rx))

# res = re.search(rx_str, test)
# # res = rx.search(test)
# print(res)

# if res:
#     print(f'{test} matches {rx_str}')
# else:
#     print('No match')

# --------------------------------- rx.search -------------------------------- #
# test = 'abc78956'
# rx = re.compile(r'[7-9]{3}')

# if rx.search(test):
#     print('ok')


# ------------------------------- rx.findall() ------------------------------- #
# test = 'hdahjda 234 jakksa 456 jfakaskfs987'
# rx = re.compile(r'\d{3}')

# res = rx.findall(test)
# for el in res:
#     print(el)

# -------------------------------- rx.split() -------------------------------- #
# test = 'a-b_c|d'
# # res = test.split('-')
# rx = re.compile(r'[_|-]')
# res = rx.split(test)
# print(res)

# --------------------------------- rx.sub() --------------------------------- #

# task: replace all digits with '*':
# test = 'gh hds43543hj 454'
# rx = re.compile(r'\d{2}')

# test_replaced = rx.sub('*',test)
# print(test_replaced)