import re

# remove commented lines
# code = """
# line1
#     # line 2
#   line3
# # line 4
# # x = 3+4
# #
#   line5
#   line6
# line7"""

# rx = re.compile(r'^\s*#.*$',re.MULTILINE)
# cleaned = rx.sub('',code )

# # remove empty lines
# cleaned = re.sub(r'(?:\n\r?){2,}','',cleaned )
# print(cleaned)

# result = """
# # line 2
# # line 4
# # x = 3+4
# #
# """


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

# TODO: make it works
rx =re.compile(r'^\s*([^#]+)\n\r?$', re.MULTILINE)
res = rx.findall(code)
print(res)
cleaned = ''.join(res)
print(cleaned)



