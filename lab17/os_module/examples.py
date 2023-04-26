import os

# Да се напише Python програма, която да покаже името на операционната система, информация за текущата информационна система

# print( os.name )
# print( os.uname().version )

#текущата директория, принтира файловете от директорията и да хвърли грешка в случай, че не съществува името на файла или пътя.

cwd = os.getcwd()
# print(cwd)


# # print( os.path.isdir('myproject')  )

# # # list only file names in CWD (текущата директория)
# content = os.listdir()

# for name in content:
# 	if not os.path.isdir(name):
# 		print(name)


base_path = '/media/nemsys/data/projects/courses/netIT/PythonCourseNetIT/PythonCourse_27.02.2023-Labs/lab17/os_module/'


# Variant1: concatenation : not good
path = base_path + 'myproject/lib'
print(path)
print( os.path.isdir(path) )

# Variant2: join - best
path = os.path.join(base_path, 'myproject/lib')
print(path)
# print( os.path.isdir(path))
