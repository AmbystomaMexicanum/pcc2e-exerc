current_users = [
	'AmbystomaMexicanum',
	'MilesFemininus',
	'Philostratus',
	'Alopecina',
	'covfefe'
]

current_users_lower = [user.lower() for user in current_users]

new_users = [
	'ambystomamexicanum',
	'PhiloStratus',
	'bill-gates',
	'ambyst0mamexicanum',
	'char1esd0ng',
	'covfefe',
	'c0vfefe'
]

for user in new_users:
	if user.lower() in current_users_lower:
		print(f"Sorry, username '{user}' is already used. Please try another one.")
	else:
		print(f"Username '{user}' available.")