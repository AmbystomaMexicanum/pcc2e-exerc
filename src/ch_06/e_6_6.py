favorite_langs = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

poll_list = ['sarah', 'phil', 'michael', 'anders']
for person in poll_list:
	if person in favorite_langs.keys():
		print(f"{person.title()}, thank you for participating in this poll.")
	else:
		print(f"{person.title()}, please take our poll!")