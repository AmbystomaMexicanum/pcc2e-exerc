term_defins = {

	'integer':
	'A number without a decimal point (.)',

	'float':
	'A number with a decimal point (.)',

	'list':
	'A data structure that stores items in a specific order',

	'dictionary':
	'A data structure that stores PAIRS of items',

	'if-test':
	'Test which results in a True/False value'

}

for term, defin in term_defins.items():
	# Seems like it's not OK in Python to break this string into multiple lines
	# (like the way it is actually printed) as in C-like languages.
	message = f"[{term}]\n{defin}.\n"
	print(message)