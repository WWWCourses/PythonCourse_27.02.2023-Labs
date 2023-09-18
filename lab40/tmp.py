# the base class
class Parent:
	def __init__(self,*args, **kwargs):
		# self = p1
		# args= [1,2,3,4]
		# kwargs = {a:3,b:4}
		print(id(self))
		print(f'{self} constructor execute')
		print(args)
		print(kwargs)
		self.x = 1

# the derived class, which inherits from base class:
class Child(Parent):
	def __init__(self, *args, **kwargs):
		# self = c
		# args = [5,6]
		# kwargs = {c:7,d:8}
		super().__init__(*args, **kwargs)

p1 = Parent(1,2,3,4,a=3,b=4)
print(id(p1))
c = Child(5,6,c=7,d=8)