def foo():
	pass


foo()

l = []

x = 1
x+1
# ----------------------------- Class Definition ----------------------------- #

# class Car:
	# pass


# ---------------------- Instantiate(create) Car object ---------------------- #
# car1 = Car()
# car2 = Car()
# car3 = Car()


# print( type(foo) )
# print( type(l) )
# print( type(x) )
# print( type(car1) )

# print( id(l) )
# print( id(car1) )
# print( id(car2) )
# print( id(car3) )

# -------------------------------- Attributes -------------------------------- #

# class Car:
# 	# Class atributes:
# 	count = 2
# 	color = 'red'

# car1 = Car()
# car2 = Car()

# # print( Car.color )
# # print( car1.color )
# # print( car2.color )


# # change calss attribute color to black
# Car.color = 'black'

# print( Car.color )
# print( car2.color )

# create car1 object attribute - not the wright way!!!
# car1.year = 2013
# car2.year = 2015
# print(car1.year)
# print(car2.year)


# ----------------------------- Method __init__() ---------------------------- #
# METHOD == Function defined in class


class Car:
	# Class atributes:
	count = 2
	color = 'white'

	# Class method
	def foo():
		print('Class method Foo')

	# Instance method
	def drive(self):
		print(f'The {self.color} is driving with {self.speed}')


	def __init__(self, year, color, speed):
		# year = 2015
		# color = '
		# print(f'Car is created for: {self}')
		# Instance attributes
		self.year = year
		self.color = color
		self.speed = speed




car1 = Car(2015, 'red', 200)
car2 = Car(color='black', year=2013, speed=230)
# Car.foo()
car1.drive() # car1.drive(car1)
car2.drive() # car2.drive(car2)

# print(Car.color)
# print(car1.color)


# print(car1.color)
# print(car2.color)