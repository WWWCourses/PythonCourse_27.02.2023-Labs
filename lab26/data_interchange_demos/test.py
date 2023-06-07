import json


# write to json:
d = {
    'name':'я'
}
json.dump(d, open('test.json','w'))

json_data = open('test.json', 'r')
data = json.load(json_data)

print(data)


