import csv

account = {
    "id": '01',
    "name":'Ada Byron',
    "balance":1000,
    "pin": '1111',
    "address": {
        'country': 'Bulgaria',
        'town': 'Sofiq'
	}
}

with open('accounts_new.csv','w') as f:
    header = account.keys()

    writer = csv.DictWriter(f, delimiter=',', fieldnames=header )
    writer.writeheader()
    writer.writerow(account)


