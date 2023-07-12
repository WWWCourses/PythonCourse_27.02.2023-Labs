import re

#  Create new list (my_fruits) which will contains each string contains the word "strawberries" or "raspberries" print the string but append "Yes!" to its end, otherwise append "No!"

strings = [
  'Ice cream with strawberries?',
  'Ice cream with blueberries?',
  'Ice cream with raspberries?',
  'Ice cream with strawraspberries?',
  'Ice cream with berries?',
]

# rx = re.compile(r'\bstrawberries\b|\braspberries\b')
rx = re.compile(r'\b(straw|rasp)berries\b')

# Variant 1
# my_fruits = []
# for string in strings:
# 	if rx.search(string):
# 		my_fruits.append(string)

#Variant 2
# my_fruits = filter(lambda string:rx.search(string), strings)
# print(list(my_fruits))

#Variant 3 - List Comprehensions
# my_fruits = [string for string in strings if rx.search(string)]
# print(my_fruits)



