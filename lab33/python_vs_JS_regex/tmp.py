import re

rx_str = r'123.abc'
text = """jkdsjkds 123
ABC
456"""

rx = re.compile(rx_str, re.I|re.S)

if rx.search(text):
    print('match')
else:
    print('no match')






