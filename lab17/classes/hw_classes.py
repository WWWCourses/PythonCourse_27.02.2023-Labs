# 1. Дефинирайте клас Human със свойства "собствено име" и "фамилно име".
# Дефинирайте клас Student, наследяващ Human, който има свойство "оценка".
# Дефинирайте клас Worker, наследяващ Human, със свойства "надница" и "изработени
# часове". Имплементирайте и метод "изчисли надница за 1 час", който смята колко
# получава работникът за 1 час работа, на базата на надницата и изработените часове.
# Напишете съответните конструктори и методи за достъп до полетата (свойства).
# A) направете списък от 10 студента
# Б) направете списък от 10 работника

class Human:
	def __init__(self, name, family) -> None:
		self.name = name
		self.family = family

class Student(Human):
	def __init__(self, name, family, score) -> None:
		super().__init__(name, family)
		# Human.__init__(self.name, family)
		self.score=score

class Worker(Human):
	def __init__(self, name, family, pay, hours) -> None:
		super().__init__(name, family)
		self.pay = pay
		self.hours = hours

	def calc_payment(self):
		payment = self.pay*self.hours
		print(f'Payment = {payment}')


pesho = Student('Petar', 'Petrov', 5)
worker1 = Worker('Wroker1', 'Workerov1', 10, 3)
worker1.calc_payment()
