# account = {
#     "id": '01',
#     "name":'Ada Byron',
#     "balance":1000,
#     "pin": '1111'
# }


# def dict_to_csv(account):
# 	data_as_csv = ''
# 	for v in account.values():
# 		data_as_csv+=str(v)+','

# 	# data_as_csv = data_as_csv.rstrip(',')
# 	data_as_csv = data_as_csv[:-1]
# 	return data_as_csv


# def csv_to_dict(csv):
# 	values = csv.split(',')
# 	d = {}
# 	d['id'] = values[0]
# 	d['name'] = values[1]
# 	d['pin'] = values[2]

# 	return d

# account_dict = csv_to_dict('01,Ada Byron,1000,1111')
# print(account_dict['name'])

# # print(account_to_csv(account))


# ---------------------------- Variant with class ---------------------------- #
class Account:
	def __init__(self) -> None:
		pass

	def create_account(self):
		self.id='01'
		self.name='Ada Byron'
		self.balance=1000
		self.pin= '1111'

	def to_csv(self):
		data_as_csv = f'{self.id},{self.name},{self.balance},{self.pin}'
		print(data_as_csv)

	def from_csv_file(self, csv_file):
		with open(csv_file,'r') as f:
			csv_str = f.read()

		values = csv_str.split(',')
		self.id = values[0]
		self.name = values[1]
		self.balance = values[2]
		self.pin = values[3]


account = Account()
account.from_csv_file('accounts.csv')
print(account.id)


