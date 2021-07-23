nums = [n for n in range(1, 10)]

for n in nums:
	if n == 1:
		suf = 'st'
	elif n == 2:
		suf = 'nd'
	elif n == 3:
		suf = 'rd'
	elif n >= 4:
		suf = 'th'
	print(f"{n}{suf}")