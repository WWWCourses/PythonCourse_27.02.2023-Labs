# ------------------------- Create set data structure ------------------------ #
# d = {
# 	'a':1,
# 	'b':2,
# 	'c':3,
# 	'a':9,
# }

# l = [1,2,3,1]

# s1 = {1,2,3,1}
# s2 = set(l)
# print(s1)
# print(s2)

### task remove repeating elements from list
# l = [1,2,1,2,1,3]
# l_uniqe_list = []

# for el in l:
# 	# if el not axists in l => append it
# 	if not el in l_uniqe_list:
# 		l_uniqe_list.append(el)

# print(l_uniqe_list) # [1,2,3]
# print(type(l_uniqe_list))


# l_uniqe_list2 = list(set(l))
# print(l_uniqe_list2)
# print(type(l_uniqe_list2))

# -------------------------------- Set Methods ------------------------------- #
### add
# s = {1,2,3}
# s.add(4)
# print(s)

# ### update
# s.update([5,3,2,1])
# print(s)

# ## task add d values into set
# d = {'a':99,'b':999}

# s.update(d)
# print(s)
# s.update(d.values())
# print(s)


### remove vs discard
s = {1,2,3}
# when element exists => no diff
# s.remove(2)
# s.discard(2)
# print(s)

# when element doesn't exists
# s.remove(9)
# s.discard(9)
# print(s)

# ------------------------------ Set Operations ------------------------------ #
### union:
# s1 = {1,2,3}
# s2 = {3,4,5}

# s_union = s1|s2
# s_union = s1.union(s2)
# s_union = s2.union(s1)
# print(s_union)

### intersection
# s1 = {1,2,3}
# s2 = {3,4,5}

# s_intersection = s1.intersection(s2)
# s_intersection = s2.intersection(s1)
# print(s_intersection)

### difference
# s1 = {1,2,3}
# s2 = {3,4,5}

# # s_diff = s1 - s2 # {1,2}
# # s_diff = s2 - s1  # {4,5}
# # s_diff = s1.difference(s2)
# print(s_diff)



# ### Tasks: Given are next data:
# facebook_friend_list = ['Maria', 'Ivan', 'Pesho']
# twitter_friend_list  = ['Maria', 'Asen']

# ## Task1: show me the names of my both facebook and twitter frends
# both_friends = list(set( facebook_friend_list) & set(twitter_friend_list) )
# print(both_friends)

# ## Task2: show me the names of my facebook or twitter frends
# all_friends_ = list(set( facebook_friend_list) | set(twitter_friend_list) )
# print(all_friends_)
# ## output: ['Maria','Ivan', 'Pesho', 'Asen']

# ## Task3: show me the twitter friends which ARE not friend in facebook
# fr = list( set(twitter_friend_list) - set( facebook_friend_list)  )
# print(fr)
# # ['Asen']









