# --------------------------------- Задача 9. -------------------------------- #
# Да се напише програма, която да брои четните и нечетните числа в даден списък от цели числа, използвайки lambda + filter и използвайки list comprehensions


### Variant 1: using list comprehensions
# l = [1,2,3,4,5]

# odds =  [el for el in l if el%2]
# evens = [el for el in l if not el%2]

# print(odds)
# print(evens)
# exit()

# print(f'Odds: {len(odds)}')
# print(f'Evens: {len(evens)}')

### Variant 2: using built in filter
l = [1,2,3,4,5]

def my_filter(el):
	# print(el)
	return el%2


odds = filter(my_filter,l)
evens = filter(lambda el:el%2==0,l)
print(list(odds))
print(list(evens))