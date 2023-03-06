# Author: Iva Popva
# print(4_0)
# print('abc')
# print('"')
# print("Jhon's pub")

# print('''line1
# line2
# line3''')

# print("""line1
# line2
# line3""")

# ------------------------------ Escape Sequence ----------------------------- #
# print('ab')
# print('a\tb')
# print('a\nb')
# print('Jhon\'s pub')
# print('x\\y')  #'x\y'

# print('line1\nline2\nline3')

# ------------------------------- Concatenation ------------------------------ #
# print( 'Hello'+' '+'World'+'!')

# -------------------------------- Repetition -------------------------------- #
# print(3*4)
# print('~'*25)
# print('3'*4)

# print('Taggle Commens: CTRL+/') # this is a comment

# --------------------------------- Immutable -------------------------------- #
# x = '3'
# y = x
# x = '2'

# RAM:
# 	 y : '3'
# 	 x : '2'

# ------------------------------ Strings Methods ----------------------------- #
# user_name_input = 'ada'
# user_name = user_name_input.capitalize()

# print(user_name_input)
# print(user_name)


# user_name = 'ada'
# user_name = user_name.capitalize()
# print(user_name)

# user_name = 'ada'.capitalize()
# print(user_name)

# txt = "I love apples, apple are my favorite fruit"
# print( txt.count("apple") )
# print( txt.count(" ") )


# ----------------------------- String Formating ----------------------------- #
# user_name = 'Ada'
# print(user_name)
# print('user_name')

### f-strings
# print('Hello ' + user_name + ', nice to see you!')
# print(f'Hello {user_name}, nice to see you!') # Hello Ada, nice to see you!

# print('{2+2}')
# print(f'{2+2}')

# ------------------------------ format() method ----------------------------- #

# x = 3.145677465
# y = 123.456
# # print(f'x = {x}')
# str1 = 'x = {:1.2f}, y={:2.2f}'.format(x,y)
# str2 = 'x = %1.2f, y=%2.2f' % (x,y)
# print(str1)
# print(str2)



# print('{}-{}'.format(1,2))
# print('{1}-{0}'.format(1,2))
# print('{1:}-{0:}'.format(1,2))



# print('{}-{}'.format(1,2))
# print('{:3d}-{:3d}'.format(1,2))
# print('{:<3d}-{:<3d}'.format(1,2))


