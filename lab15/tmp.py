# ------------------------- with list of dictionaries ------------------------ #
# ford = {
# 	"year": 2013,
# 	"speed": 250,
# 	"price": 1000
# }

# bmw = {
# 	"year": 2015,
# 	"speed": 240,
# 	"price": 1200
# }

# print(bmw['year'])

# # cars = [ford, bmw]
# # def find_cheepest_car(cars):
# # 	pass


class Car:
	def __init__(self,year,speed,price):
		print('Car is constructed')
		self.speed = speed
		self.year = year
		self.price = price


ford = Car(2013,250,100)
bmw = Car(2015,240,1200)

print( bmw.price )
