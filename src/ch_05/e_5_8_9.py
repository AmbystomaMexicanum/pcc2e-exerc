# Exerc. 5-8 & 5-9 combined.

# For exerc. 5-8:
users = [
	'admin',
	'Jaden',
	'AmbystomaMexicanum',
	'MilesFemininus',
	'Origo',
	'covfefe'
]

# For exerc. 5-9:
# users = []

# Common part:
if users:
	for user in users:
		if user == 'admin':
			print('Hello admin, would you like to see a status report?')
		else:
			print(f'Hello {user}, thank you for logging in again.')
else:
	print('We need to find some users!')