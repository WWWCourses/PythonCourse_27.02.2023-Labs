import re


tests = [
    'abc',
    'abbbc'
]



# for test in tests:
#     if re.search(r'ab*c',test):
#         print('ok')

rx = re.compile(r'ab*c')
for test in tests:
    if rx.search(test):
        print('ok')