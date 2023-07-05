import re

# Task: find all cats:
test = 'my cat loves dogs. The dog is ... Caterpilat, cats'
rx = re.compile(r'cats? #match cat r cats', re.I|re.VERBOSE)
rx = re.compile(r'(?ix)cats? #match cat r cats',)

res = rx.findall(test)
print(res)

# res = ['cat',  'Cat', cats]

