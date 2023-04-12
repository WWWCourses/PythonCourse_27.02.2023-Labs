# --------------------------------- Задача 8. -------------------------------- #
# Да се напише програма, която да намира сечението на два списъка използвайки lambda.
get_intersection = lambda l1,l2:set(l1).intersection(set(l2))

l1 = [1,2,3,2]
l2 = [2,3,4]

# a = set(l1)
# b = set(l2)
# print(a.intersection(b))

print( get_intersection(l1,l2) )
