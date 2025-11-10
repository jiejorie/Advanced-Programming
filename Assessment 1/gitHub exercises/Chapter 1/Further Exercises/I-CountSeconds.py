# EXERCISE I: COUNT SECONDS
print("Count Seconds")
days = int(input("\nEnter a number of days to convert into seconds: "))

daysToHours = days*24
hoursToSeconds = daysToHours*(60**2)

print(f"\nThere are {hoursToSeconds} seconds in {days} days!")
