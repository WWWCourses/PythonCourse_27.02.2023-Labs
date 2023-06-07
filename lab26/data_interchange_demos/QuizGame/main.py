import json


def add_q_and_a():
	q = input('Enter a question:')
	a = input('Enter answer:')

	q_num=len(q_and_a)
	q = f'{q_num+1}.{q}'
	q_and_a[q]=a

def to_json(data):
	f = open(json_file, 'w')
	json.dump(data, f)


json_file = 'data.json'

q_and_a = json.load(open(json_file,'r'))

add_q_and_a()

for q, a in q_and_a.items():
	print(f'{q} - {a}')

to_json(q_and_a)




