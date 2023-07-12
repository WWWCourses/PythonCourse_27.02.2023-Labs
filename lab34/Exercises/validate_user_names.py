# A valid user name must follow next rules

# Must consists of 3 to 10 characters inclusive.
# Username can only contain alphanumeric characters, dashes (-) and underscores (_).
# The first character of the username must be an alphabetic character

user_names = user_names = [
  "ada", 	# yes
  "a__", 	# yes
  "a12345",	# yes
  "a1234567890", # no (rule 1)
  "1aaaaaaa",	# no (rule 3)
  "aaa#", 	# no (rule 2)
  "a", 		# no (rule 1)
]

rx = re.compile(r'[a-zA-Z\d_-]')
rx = re.compile(r'^[a-zA-Z][\w-]{2,9}$')