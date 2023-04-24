# ---------------------------------- Methods --------------------------------- #

# class Car:
# 	# Class atributes:
# 	counter = 0

# 	# Class method
# 	def count():
# 		Car.counter+=1
# 		print('Class method count')

# 	# Instance method
# 	def drive(self):
# 		print(f'The {self.color} is driving with {self.speed}')



# 	def __init__(self, year, color, speed):
# 		# Instance attributes
# 		self.year = year
# 		self.color = color
# 		self.speed = speed

# 		Car.count()



# car1 = Car(2015, 'red', 200)
# car2 = Car(color='black', year=2013, speed=230)
# car3 = Car(color='blue', year=2010, speed=180)

# print('hi')
# print(Car.counter)

# car1.drive()

# Dog:
# 	age: 5

# dog1:
# 	age: 6

# Example:
# class Dog():
# 	age=5

# 	def happy_burthday(self):
# 		print(self.age)
# 		self.age = self.age + 1

# dog1 = Dog()
# dog2 = Dog()

# dog1.happy_burthday()

# print(dog1.age)
# print(dog2.age)

# -------------------------- Dunder (Magic) Methods -------------------------- #
class A:
	def __init__(self, id) -> None:
		self.id = id

	def __str__(self):
		return f'Object with id: {self.id}'

a1 = A(1)

# print( a1.__str__() )
print(a1)

# print( dir(a1) )


