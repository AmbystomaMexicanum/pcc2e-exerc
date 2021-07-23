person = {
	'first_name': 'Origin',
	'last_name': 'Chen',
	'age': 18,
	'city': 'Guangzhou'
}

# `person.items()`, not `person` only!
for k, v in person.items():
	print(f"Key: {k}")
	print(f"Value: {v}\n")