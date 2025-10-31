# EXERCISE 5: CONTINUE
print("Continuous Loop")
user_input = ""
loop = 0
while user_input != "y":
    loop +=1
    user_input = input("\nWould you like to continue? Enter 'y' to Quit.\n").lower()

print(f"\nThe loop was executed {loop} times")
