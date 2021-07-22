destinations = ['Estonia', 'Finland', 'Antarctica', 'Sweden', 'Norway']
print(f'Original list:\n{destinations}')

print(f'Sorted list:\n{sorted(destinations)}')
print(f'Original list:\n{destinations}')

print(f'Sorted list reversed:\n{sorted(destinations, reverse=True)}')
print(f'Original list:\n{destinations}')

destinations.reverse()
print(f'Original list reversed:\n{destinations}')
destinations.reverse()
print(f'Original list reversed twice:\n{destinations}')

destinations.sort()
print(f'Original list sorted:\n{destinations}')
destinations.sort(reverse=True)
print(f'Original list sorted reversed:\n{destinations}')