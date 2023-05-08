import os
# import mod1 as mod1

# y = mod1.x + 1


file_dir = os.path.dirname(__file__)
abs_file_dir = os.path.abspath(file_dir)

print(__file__)
print(file_dir)
print(abs_file_dir)