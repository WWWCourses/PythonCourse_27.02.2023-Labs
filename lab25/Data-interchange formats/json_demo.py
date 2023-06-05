import json

account = {
    "id": '01',
    "name":'Ada Byron',
    "balance":1000,
    "pin": '1111',

}

json_file = open('accounts.json','w')
# data_json = json.dumps(account)
json.dump(account, json_file)


json_file = open('accounts.json','r')
account_dict = json.load(json_file)
print(account_dict['name'])


# data_json = """
# 	{
# 		"id": '01',
# 		"name":'Ada Byron',
# 		"balance":1000,
# 		"pin": '1111',
#         "male":false
# 	}
# """