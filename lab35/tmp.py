import re

### Variant 2:
code = """
line1
    # line 2
  line3
# line 4
# x = 3+4
#
  line5
  line6
line7"""

# TODO: make it works - DONE
rx =re.compile(r'^\s*([^#\n]+)$', re.MULTILINE)
res = rx.findall(code)
# print(res)
cleaned = '\n'.join(res)
print(cleaned)

