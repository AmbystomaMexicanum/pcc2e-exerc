# 1: False
print('python' == 'Python')

# 2: True
print('python' == 'Python'.lower())

my_age = 18
# 3: True
print(my_age == 18)
# 4: True (adult)
print(my_age >= 18)
# 5: False
print(my_age > 18)

depressed = True
# 6: True
print(depressed)
# 7: True (a depressed adult)
print(my_age >= 18 and depressed)

my_problems = ['depression', 'OCD']
# 8: True
print('OCD' in my_problems)
# 9: False
print('ocd' in my_problems)
# 10: True
print('ocd'.upper() in my_problems)
# 11: True
print('insomnia' not in my_problems)

# Settling my problems (which I kind of hoping to...)
my_problems.pop()
my_problems.pop()
# 12: False
if my_problems:
	print('You still have problems. Keep on tackling them!')
else:
	print('You are fine now. Congrats.')

# Estimated outputs:
#
# False
# True
# True
# True
# False
# True
# True
# True
# False
# True
# True
# You are fine now. Congrats.