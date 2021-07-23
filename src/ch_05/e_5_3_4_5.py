# 5-3

alien_color = 'green'
# Alt. ver.:
# alien_color = 'yellow'

if alien_color == 'green':
	print('You get 5 points.')

# 5-4

alien_color = 'green'
# Alt. ver.:
# alien_color = 'yellow'

if alien_color == 'green':
	points = 5
else:
	points = 10

print(f"You get {points} points.")

# 5-5

alien_color = 'yellow'
# Alt. ver.:
# alien_color = 'green'
# alien_color = 'red'

if alien_color == 'green':
	points = 5
elif alien_color == 'yellow':
	points = 10
elif alien_color == 'red':
	points = 15
# else:
#	print('Unidentifiable alien')

print(f"You get {points} points.")