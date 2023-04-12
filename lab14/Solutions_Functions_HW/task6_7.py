# --------------------------------- Задача 6. -------------------------------- #
# Да се напише програма, която да сортира списък от tuples използвайки Lambda.

# def mysort(t):
# 	return t[1]

# def sort_LoT(l):
# 	sorted_l = sorted(l,key=lambda t:t[1])
# 	return sorted_l

# input_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print( sort_LoT(input_list) )



# --------------------------------- Задача 7. -------------------------------- #
# Да се напише програма, която да сортира списък от речници използвайки Lambda. Sort by 'price' value
# from pprint import pprint

# input_list = [
# 	{
# 		'product':'Bread',
# 		'price':2
# 	},
# 	{
# 		'product':'Wine',
# 		'price':3
# 	},
# 	{
# 		'product':'Beer',
# 		'price':1
# 	}
# ]

# pprint( sorted(input_list, key=lambda d: d['price']))

# -------------------------------- BONUS TASK: ------------------------------- #
# write function which will sort the dictionary by given key.
from pprint import pprint

def sort_LoD_by_key(lod,key_name='price'):
	print(f'Sorted by {key_name}:')
	pprint( sorted(lod, key=lambda d:d[key_name]) )
	print()

input_list = [
	{
		'product':'Bread',
		'price':5
	},
	{
		'product':'Wine',
		'price':3
	},
	{
		'product':'Beer',
		'price':1
	}
]

sort_LoD_by_key(input_list)
sort_LoD_by_key(input_list, 'price')
sort_LoD_by_key(input_list, 'product')
