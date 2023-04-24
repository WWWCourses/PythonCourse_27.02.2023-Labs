
# --------------------------- Example: BankAccount --------------------------- #

# pesho:
# 	name: Pesho
# 	age: 24
# 	password: 123

class User:
	def __init__(self, name, age) -> None:
		self.name = name
		self.age = age

	def registrate(self):
		pw = '123'
		self.password = pw


	def login(self):
		pass


class Account:
	def __init__(self, user) -> None:
		self.__balance = 0
		self.__user = user

	def setBalance(self, value):
		# chack value...
		self._balance += value

	def getBalance(self):
		return self._balance

	def deposit(self, value):
		# log into db
		self.setBalance(value)

	def withdraw(self, value):
		self.setBalance(-value)



# ----------------------------------- main ----------------------------------- #
pesho = User('Pesho', 24)
pesho.registrate()

pesho_account = Account(pesho)
# pesho_account.deposit(100)
# pesho_account.withdraw(50)
pesho_account.__balance = 0




# print( pesho_account.getBalance() )




