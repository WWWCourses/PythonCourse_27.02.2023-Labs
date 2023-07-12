import re

# Task print the name and the phone only of the BG phone numbers (+359 XXXXXXXXX)

"maria:+359881234567"
"ivan:+359887654321"

tests = [
	'maria:+359 881234567',
	'asen:  +123 881234567',
	'ivan:   +359    887654321',
]

rx = re.compile(r'^(\w+):\s*\+359\s+(\d{9})')

for test in tests:
	m = rx.search(test)
	# print(m)
	if m:
		# print(f"{m.group(1)}:+359{m.group(2)}")
		# name, phone = m.group(1,2)
		name, phone = m.groups()
		print(f'{name}:+359{phone}')


