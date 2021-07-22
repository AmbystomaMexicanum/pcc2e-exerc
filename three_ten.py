languages = ['Portuguese', 'Spanish', 'Russian', 'Japanese', 'Arabic', 'Ancient Greek', 'Modern Greek', 'Latin']
print(f"List of languages: {languages}")

# .append()
languages.append('Nahuatl')
languages.insert(5, 'Maori')

# .pop()
popped_lang = languages.pop()
print(f"Now I think of it, I don't want to learn {popped_lang} now.")

# .remove()
removed_lang = 'Latin'
print(f"Now I think of it, I'm not very interested in {removed_lang} either.")

# sorted()
sorted_langs = sorted(languages)
print(f"Languages sorted (using sorted()): {sorted_langs}")

# .sort()
languages.sort()
print(f"Languages sorted (using .sort()): {languages}")

# .reverse()
languages.reverse()
print(f"Languages reversed: {languages}")

# len()
print(f"I want to learn {len(languages)} languages at this moment.")