import re


rx = re.compile(r'''
a #match symbol 'a'
\s #match any whitespace character
b # match symbol 'b'
''', re.X)
# r'a\sb'

test = """bela bartok"""

if rx.search(test):
    print('Match')
else:
    print('No Match')