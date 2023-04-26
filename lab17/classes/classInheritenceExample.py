class Animal:
	def __init__(self, name, age) -> None:
		if age<0:
			print('Wrong age')
			exit()

		self.name = name
		self.age = age

	def make_sound(self):
		print( f'{self.name} say {self.sound}' )


class Dog(Animal):
	sound = 'Bau bau'


class Cat(Animal):
	sound = 'Myauuu'
	def __init__(self, name, age, color) -> None:
		super().__init__(name, age)
		self.color = color

	def make_sound(self):
		print( f'The {self.color} cat named {self.name} say {self.sound}' )


# create instance
dog1 = Dog('Sharo', 3)
dog1 = Dog('Balkan', 2)
cat1 = Cat('Tom', 2, 'black')

# use objects
dog1.make_sound()
cat1.make_sound()



