# Note:
# 1. In Italian 'pizza' has the plural form 'pizze';
# 2. I don't know much pizze; fill it in if you can.

pizze = ['pepperoni', 'pizza no. 2', 'pizza no. 3']
friend_pizze = pizze[:]

pizze.append('pizza no. 4')
friend_pizze.append('pizza no. 5')

print('My favorite pizze are:\n')
for pizza in pizze:
	print(pizza.title())
print()

print("My friend's favorite pizze are:\n")
for friend_pizza in friend_pizze:
	print(friend_pizza.title())
print()
