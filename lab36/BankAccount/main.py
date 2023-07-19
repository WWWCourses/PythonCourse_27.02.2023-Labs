import json
from pymongo import MongoClient
from pprint import PrettyPrinter

printer = PrettyPrinter()

# Connect to DB:
# client = MongoClient('mongodb://Iva:1234@127.0.0.1:27017')
client = MongoClient("mongodb+srv://PythonCourse:12345678abv@cluster0.qprcu.mongodb.net/?retryWrites=true&w=majority")

# Create 'BankAccount'
db = client.BankAccount

# Create document
def create_user(user_name, balance):
	res = db.Users.insert_one({
			"user":user_name,
			"balance":balance
	})

create_user('MArin', 2222)

def create_users_from_lists():
	user_names = ['Maria2','Ivan2']
	user_balances = [1000, 400]

	for user,balance in zip(user_names,user_balances):
		print(user,balance)
		db.Users.insert_one({
			"user": user,
			"balance":balance
		})

	print(list(zip(user_names,user_balances)))


# Read:
def get_user():
	printer.pprint(db.Users.find_one())

# get_user()

# get user with user:"Ivan"
# printer.pprint( list(
# 	db.Users.find({"user":"Ivan"},{"_id":0,"user": 1})
# ))

# get user names of users with balance>200
# printer.pprint( list(
# 	db.Users.find({"balance":{"$gt":200}},{"_id":0,"user": 1})
# ))

# get users with balance>200 and user name starts with "I"

printer.pprint( list(
	db.Users.find(
		{
			"$and":[
				{
					"balance":{"$gt":300}
				},
				{
					"user":{
						"$regex":r"^I"
					}
				}
			]
		},
		{"_id":0})
))



