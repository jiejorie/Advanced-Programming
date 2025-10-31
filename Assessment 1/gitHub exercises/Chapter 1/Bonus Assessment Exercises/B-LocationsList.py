# EXERCISE B: LOCATIONS LIST
print("Locations List")
locations =['dubai','paris', 'switzerland', 'London', 'amsterdam', 'New York']

print(f"\nList: {locations}\nLength of the list: {len(locations)}")

print(f"\nAlphabetically sorted: {sorted(locations)}\nOriginal list (unmodified): {locations}")

locations.reverse()
print(f"\nReversed list: {locations}")

locations.sort()
print(f"\nAlphabetically sorted: {locations}")

locations.sort(reverse=True)
print(f"\nReversed alphabetical order: {locations}")
