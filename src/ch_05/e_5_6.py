age = 18

if age < 2:
	phase = 'baby'
elif age < 4:
	phase = 'infant'
elif age < 13:
	phase = 'child'
elif age < 20:
	phase = 'teenager'
elif age < 65:
	phase = 'adult'
elif age >= 65:
	phase = 'senior'

print(f'You are a(n) {phase}.')