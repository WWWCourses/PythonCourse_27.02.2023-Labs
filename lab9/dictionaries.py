# l = [1,2,3]
# l[4] = 9
# print(l[4])

# ---------------------- Add or change dictionary values --------------------- #
# d = {
# 	'a':1,
# 	'b':2
# }

# # print( d['c']) # ERROR
# d['c'] = 3
# d['a'] = 9
# print(d)

# ------------------------ Remove dictionary elements ------------------------ #
# d = {
# 	'a':1,
# 	'b':2
# }

# ### remove element with key 'a'
# ## using del:
# # del d['a']
# # print(d)

# ## using pop
# res = d.pop('c')
# print(d)
# print(res)


### example 1
# user_data = {
# 	'ivan':'08881234',
# 	'pesho':'08881235'
# }

# tel = user_data.pop('maria', '0000000')
# print(user_data)
# print(tel)

# ------------------------------ Copy Dictionary ----------------------------- #
# d = {
# 	'a':1,
# 	'b':2
# }

# d_copy = d.copy()

# d['a'] = 9

# print(d)
# print(d_copy)

# ---------------------------- Sorting Dictionary ---------------------------- #
# l =[3,1,2]
# print( sorted(l))

# d = {
# 	'b':2,
# 	'a':1,
# 	'c':3
# }

# # sort keys
# print( sorted(d) )
# # sort values
# print( sorted(d.values()) )

# print(d)


# --------------------------- Loop over dictionary --------------------------- #
# d = {
# 	'b':2,
# 	'a':1,
# 	'c':3
# }

###
# for key in d:loop on keys
# 	print(key)

# for key in d.keys():
# 	print(key)

# print( d.keys() )
# print( d.values() )

### loop on values:
# for val in d.values():
# 	print(val)

# for key in d:
# 	val = d[key]
# 	print(val)


### loop on key and values:
d = {
	'b':2,
	'a':1,
	'c':3
}

# for key in d:
# 	val = d[key]
# 	print(f'{key}-{val}')

# for key,val in d.items():
# 	print(f'{key}-{val}')





