# ---------------------------------- Slicing --------------------------------- #
# l = [1,2,3,4,5]
# print(l[-2]) # indexing
# print(l[-6])

# start = 2
# end = -6
# step = -2

# print( l[start:end:step] )
# # print(list(range(start,end,step)))
# # # [2, 0,-2, -4]

# print( l[-1:-4:-1] ) # [5,4,3]

### reverse list:
# reversed_list = l[::-1]
# print(reversed_list)

### reverse string:
# word = 'test'
# reversed_word = word[::-1]
# print(reversed_word)

# ---------------------------- Some lists methods ---------------------------- #
# l = [1,2,3]
# l.append(4)
# print(l)

# l1 = [1,2,3]
# l2 = [4,5]
# l1.extend(l2)
# print(l1)

# l1 = [1,2,3]
# tmp = 'abc'
# l1.extend(tmp)
# print(l1)

# l1 = [1,2,3,2]
# l1.remove(2)
# print(l1)

# l1 = [1,2,3,4,5]
# el = l1.pop(-2)
# print(l1)
# print(el)

# list.index(x[, start[, end]])
# l1 = [1,2,3,4,5]
# i = l1.index(3)
# print(i)

# l = [1,2,3,4,5]
# l.reverse()
# print(l)
# l_rev = l[::-1]
# print(l_rev)
# print(l)

# l = [1,2,3]
# x = 9
# l.insert(1,x)
# print(l)

### Sum elements of list:
# l = [1,2,3]
# sum = 0
# for num in l:
# 	sum+=num

# # print(sum)
# print(min(l))
# print(max(l))

# --------------------------------- Use lists -------------------------------- #
# Task: user enters student names and scores. Find the name of the student with highest score:
#
# Maria - 3,
# Ivan -  5,
# Pesho - 4
### Output:
# 'Ivan has highest score: 5'

# student_names = []
# student_scores = []

# # student_name = input('Enter student name: ')
# # student_score = input('Enter student score: ')
# # user_answer = input('Will you enter more[y/n]: ')

# while True:
# 	student_name = input('Enter student name: ')
# 	student_score = input('Enter student score: ')
# 	student_names.append(student_name)
# 	student_scores.append(student_score)

# 	user_answer = input('Will you enter more[y/n]: ')
# 	if user_answer=='n':
# 		break

# print(student_names)
# print(student_scores)

# max_score = max(student_scores)
# max_score_index = student_scores.index(max_score)

# print(f'{student_names[max_score_index]} has highest score: {max_score}')


# --------------------------------- sort list -------------------------------- #
# l1 = [3,2,4,6]
# l2 = sorted(l1, reverse=True)
# print(l2)

# l1 = [3,2,4]
# l2 = l1 # l2 IS NOT A COPY,
# l1.sort(reverse=True)
# print(l1)  # [4,3,2]
# print(l2)  # [4,3,2]


# l1 = [3,2,4]
# l2 = l1[::] # l2 IS  A COPY,
# l1.sort(reverse=True)
# print(l1)  # [4,3,2]
# print(l2)  # [3,2,4]



# word = 'adbfc'
# word_sorted_list = sorted(word) # ['a', 'b', 'c', 'd', 'f']
# word_sorted = '-'.join(word_sorted_list)
# print(word_sorted)

# ------------------------------- operator 'in' ------------------------------ #
# l = [1,2,3,4]
# print( 2 in l)
# print( 2 not in l)

l = [3,2,3,2,2,4]
# while 2 in l:
# 	l.remove(2)

# print(l)

### TODO: while l is not defined
# for el in l:
# 	del(l,el)
# print(l)

# l = [3,2,3,2,2,4]
# l2 = list(filter(lambda el: el!=2, l))
# print(l2)

# l = [3,2,3,2,2,4]
# l2 = [el for el in l if el!=2]
# print(l2)







