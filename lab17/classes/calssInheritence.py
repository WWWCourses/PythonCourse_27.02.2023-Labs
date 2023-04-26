class A:
	# id = 1
	def __init__(self,id) -> None:
		self.id = id

class B():
	# pin =1234

	def __init__(self,pin) -> None:
		self.pin = pin

class C(A,B):
	def __init__(self,id, pin):
		A.__init__(self, id)
		B.__init__(self, pin)
		# super().__init__(id)
		# super(B).__init__(pin)

c = C(1, 1234)

print(c.id)
print(c.pin)