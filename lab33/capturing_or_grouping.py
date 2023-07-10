import re

rx = re.compile(r'(0[7-9]{2})\s(\d{6})')
test = '087 123456'

res = rx.search(test)
print(res.groups())
