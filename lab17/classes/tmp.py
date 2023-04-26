class Student:
	country = 'Bulgaria'
	name = 'Anonymous'

	def __init__(self, name) -> None:
		self.name = name

	def __str__(self):
		return f'name: {self.name}\ncountry: {self.country}'

student1 = Student('Pesho')
student2 = Student('')

print(student1)
print(student2)
print(Student.name)
print(Student.country)
