rivers = {
	'nile': 'egypt',
	'yangtze': 'china',
	'ob': 'russia',
	'mississippi': 'america',
	'thames': 'england',
	'seine': 'france'
}

for river, country in rivers.items():
	print(f"The {river.title()} river runs through {country.title()}.")