foods = ('noodles', 'rice', 'lettuce', 'chicken', 'tomato')
print('Original menu:\n')
for food in foods:
	print(food)

# Could trigger an Python error:
# foods[1] = 'bread'

foods = ('noodles', 'bread', 'lettuce', 'beef', 'tomato')
print('\nNew menu:\n')
for food in foods:
	print(food)
