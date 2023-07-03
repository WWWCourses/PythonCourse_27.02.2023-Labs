import re


tests = [
	'0',   # no
    'ab',  #'ok'
    'sad3', # no
    '1234',  # no
    ' ',    # ok
]


# strings, which have non-digit symbols:
rx=r'[^0-9]'

for test in tests:
    if re.search(rx,test):
        print(f'{test} # ok')
    else:
        print(f'{test} # no')




