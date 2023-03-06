# print( 3*4 )

# RAM:
# 	0x123: 0011(3)
# 	0x124: 0100(4)

# ------------------------- Calculate VAT for a price ------------------------ #
# base price = 100 lv
# price with vat = base price * 1.2

# основна_цена = 100
# print( основна_цена *1.2)

# base_price = 100
# price_with_vat = base_price * 1.2
# print( price_with_vat )

# ---------------------------- Assignment Operator --------------------------- #
# x = 2
# y = 2

# print( id(2) )
# print( id(x) )
# print( id(y) )

# RAM:
# 	x,y: 0x123: <0010 (2), int,>


# --------------------------------- Example 1 -------------------------------- #
# x = 3
# y = x
# x = 2

# print(x)  # 2 | 2
# print(y)  # 2 | 3


# # RAM:
# # 	y: 	<0101 (3), int>
# # 	x : <0110 (2), int>

# --------------------------------- Example 2 -------------------------------- #
# x = 1
# x = 2
# x = 3

# print(x)

# RAM:
# 	#  : 1
# 	#  : 2
# 	x  : 3



