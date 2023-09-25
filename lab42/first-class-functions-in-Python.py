class A:
	def connect(self, f, *args):
		print('Connect will execute f with args:')

		f(*args)

	def clickedAction(self, *args):
		print('clickedAction is called with args:')
		print(args)





a = A()
# res = a.clickedAction()
# print(res)


print('Start')
a.connect( a.clickedAction, 1,2,3 )
print('End')


