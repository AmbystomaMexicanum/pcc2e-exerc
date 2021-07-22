# Exercises 3-4 to 3-7 and 3-9 as one single .py code file.

# 3-4

dinner_invitees = ['Xu Fengcan', 'Song Xi', 'Origin Chen', 'Joan of Arc', 'El Cid', 'Gaius Octavius']

print(f'Respected soldier {dinner_invitees[0]}, please come to me for dinner.')
print(f'Respected veteran {dinner_invitees[1]}, please come to me for dinner.')
print(f'Dear {dinner_invitees[2]}, please come to me for dinner.')
print(f'Respected heroine {dinner_invitees[3]}, please come to me for dinner.')
print(f'Respected "sayyid" {dinner_invitees[4]}, please come to me for dinner.')
print(f'Augustus {dinner_invitees[5]}, please come to me for dinner.')
print(f'Current number of guests: {len(dinner_invitees)}')
print()

# 3-5

unavailable_invitee = dinner_invitees.pop()
print(f'Sorry, for certain reasons, {unavailable_invitee} is not able to come to dinner.')
dinner_invitees.append('Constantine XI')
print(f'The unavailable invitee {unavailable_invitee} is now replaced by {dinner_invitees[-1]}.')
print('Re-printing invitation messages, as follows...')
print()

print(f'Respected soldier {dinner_invitees[0]}, please come to me for dinner.')
print(f'Respected veteran {dinner_invitees[1]}, please come to me for dinner.')
print(f'Dear {dinner_invitees[2]}, please come to me for dinner.')
print(f'Respected heroine {dinner_invitees[3]}, please come to me for dinner.')
print(f'Respected "sayyid" {dinner_invitees[4]}, please come to me for dinner.')
print(f'Autocrator {dinner_invitees[5]}, please come to me for dinner.')
print(f'Current number of guests: {len(dinner_invitees)}')
print()

# 3-6

print('A bigger table is found. Thus 3 new persons would be invited.')
print()

dinner_invitees.insert(0, 'Bill Gates')
dinner_invitees.insert(3, 'Hua Mulan')
dinner_invitees.append('Albert Einstein')

print(f'Welcome to dinner, {dinner_invitees[0]}!')
print(f'Welcome to dinner, {dinner_invitees[1]}!')
print(f'Welcome to dinner, {dinner_invitees[2]}!')
print(f'Welcome to dinner, {dinner_invitees[3]}!')
print(f'Welcome to dinner, {dinner_invitees[4]}!')
print(f'Welcome to dinner, {dinner_invitees[5]}!')
print(f'Welcome to dinner, {dinner_invitees[6]}!')
print(f'Welcome to dinner, {dinner_invitees[7]}!')
print(f'Welcome to dinner, {dinner_invitees[8]}!')
print(f'Current number of guests: {len(dinner_invitees)}')
print()

# 3-7

print('Sorry! The new-bought table cannot be delivered in time! Now only 2 persons can be invited now.')
print()

popped_invitee = dinner_invitees.pop()
print(f"I'm sorry {popped_invitee}, but I cannot invite you over for dinner.")
popped_invitee = dinner_invitees.pop()
print(f"I'm sorry {popped_invitee}, but I cannot invite you over for dinner.")
popped_invitee = dinner_invitees.pop()
print(f"I'm sorry {popped_invitee}, but I cannot invite you over for dinner.")
popped_invitee = dinner_invitees.pop()
print(f"I'm sorry {popped_invitee}, but I cannot invite you over for dinner.")
popped_invitee = dinner_invitees.pop()
print(f"I'm sorry {popped_invitee}, but I cannot invite you over for dinner.")
popped_invitee = dinner_invitees.pop()
print(f"I'm sorry {popped_invitee}, but I cannot invite you over for dinner.")
popped_invitee = dinner_invitees.pop()
print(f"I'm sorry {popped_invitee}, but I cannot invite you over for dinner.")
print()

print(f"Current list: {dinner_invitees}")
print(f'Current number of guests: {len(dinner_invitees)}')
print()
print(f"Don't worry {dinner_invitees[0]}, you are still on the list!")
print(f"Don't worry {dinner_invitees[1]}, you are still on the list!")
print()

del dinner_invitees[0]
del dinner_invitees[0]

print(f"Current list: {dinner_invitees}")
print(f'Current number of guests: {len(dinner_invitees)}')
