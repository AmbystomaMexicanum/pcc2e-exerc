numlist = [val**2 for val in range(0, 10)]
print(f'Popped element:\n{numlist.pop()}\n')
print(f'List now:\n{numlist}\n')

print(f'First three elements:\n{numlist[:3]}\n')
print(f'Last three elements:\n{numlist[-3:]}\n')
print(f'Elements in the middle:\n{numlist[3:-3]}\n')
