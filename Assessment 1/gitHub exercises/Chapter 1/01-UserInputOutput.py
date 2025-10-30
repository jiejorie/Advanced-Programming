# EXERCISE 1: USER INPUT OUTPUT
print("Hello, user!")
userName = input("What is your name?\n").title()
while True:
    try:
        userAge = int(input("What is your age?\n"))
        break
    except ValueError:
     print("Error: Please enter a number for your age.\n")
print(f"It is good to meet you, {userName}")
print(f"The length of your name is:\n{len(userName)}")
print(f"You will be {userAge+1} in a year.")