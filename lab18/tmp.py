import os

cwd = os.getcwd()
print(cwd)

paths = os.path.split(cwd)
print(paths)