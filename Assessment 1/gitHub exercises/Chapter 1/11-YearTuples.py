# EXERCISE 11: YEAR TUPLES
print("Year Tuples")
year = (2017,2003,2011,2005,1987,2009,2020,2018,2009)

print(f"\nAcessing the -3 index value: {year[-3]}")
print(f"Original tuple order: {year}")
print(f"\nReversed tuple order: {sorted(year, reverse=True)}")
print(f"\nNo. of times 2009 is repeated: {year.count(2009)}")
print(f"\nIndex value of 2018: {year.index(2018)}")
print(f"\nLength of tuple: {len(year)}")
