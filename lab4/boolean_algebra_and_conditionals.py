# ------------------------------- Boolean Type ------------------------------- #
# print( type(5) )
# print( type('5') )
# print( type(True) )

# x = 4
# print(type(x))


# print( bool('') )
# print( bool(' ') )

# print( int('3') )

# print( bool(-0.03) )

# ---------------------------- Logical Operations ---------------------------- #
# A: навън вали => True
# B: навън грее слънце => Fasle

# A and B => False
# A or B  => True

# print( True and False)
# print( True or False)
# print( not True)

# # x or y:	if x is false, then y, else x
# print( True or True )			# True
# print( True or False )		# True
# print( False or True )		# True
# print( False or False )		# False
# print('*'*20)

# # x and y:	if x is false, then x, else y
# print( True and True )		# True
# print( True and False )		# False
# print( False and True )		# False
# print( False and False )	# False
# print('*'*20)

# # not x	if x is false, then True, else
# print( not True)
# print( not False)
# print('*'*20)

# print( 0 and 5 ) # 0
# print( 2 or 3 )  # 2
# print( 2 or 0 )  # 2
# print( 3 and 0)  # 0

# --------------------------- Comparison Operations -------------------------- #
# x = 1
# y = 5

# print( x>y ) 			# False
# print( x<y ) 			# True
# print( x==y ) 			# False

# print( 3<3 ) # False
# print( 3<=3 ) # True

# print( 3==3 )
# print( 3!=3 )

# # user_age = '16'
# user_age = int(input('Enter age: '))

# print( user_age >= 18 )

# print( '9' < '1' )      #False
# print( 57 < 49 )     	#False

# print( '9' < '100' )
# print( '9a' < '1_00' )
# # print( '9' < '1' )  => Flase

# print( '9' < '900')   # True
# # print( '9' < '9')
# # print( '' < '0')  => True

# print( 'мария'>'пешо') # False
# print( 'мария'>'Пешо') # True


# -------------------------- Control Flow Statements ------------------------- #

# Statement vs Expresion
# 2+3 # expression
# print( 2+3 )

# #
# x=3 # statement
# print( x=3 )


### IF:
# if expression :
#   block 1

# user_age = int( input('Enter age: ') )
# if user_age>=18:
# 	print('Welcome')

# print('End')


### IF-ELSE:
# user_name = input('Enter name:')

# if user_name is equal to '' => 'Anonumous'
# if user_name:
# 	pass
# else:
# 	user_name = 'Anonymous'

# print(f'Hello, {user_name}')
# if user_name == '':
# 	user_name = 'Anonymous'

# if not user_name:
# 	user_name = 'Anonymous'

# print(f'Hello, {user_name}')

# # print( 5 == False )

### Task1 ( 0 is even )
#if x is even => print('Even')
#if x is odd => print('Odd')
# x = 9

# if x%2==0:
# 	print('Even')
# else:
# 	print('Odd')

# x = 8
# if x%2:
# 	print('Odd')
# else:
# 	print('Even')


### IF-ELIF-ELSE:
### task
#if x is even => print('Even')
#if x is odd => print('Odd')
#if x is 0 => print('Don\'t know!!!')

## variant 1
# x = 8
# if x == 0:
# 	print('Don\'t know!!!')
# else:
# 	if x%2==0:
# 		print('Even')
# 	else:
# 		print('Odd')

## variant 2 - better than variant 1
# x = 8
# if x == 0:
# 	print('Don\'t know!!!')
# elif x%2==0:
# 	print('Even')
# else:
# 	print('Odd')

### example
# user_lang = "hu"
# if user_lang == "bg":
#     print("Здравейте")
# elif user_lang == "it":
#     print("Ciao")
# elif user_lang == "en":
#     print("Hello")
# else:
# 	print("I do not speak your language!")









