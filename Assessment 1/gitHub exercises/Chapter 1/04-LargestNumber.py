# EXERCISE 4: LARGEST NUMBER
print("Checking for the Largest Number")

while True:
    try:
        firstNum = float(input("\nPlease enter your first number: \n"))
    except ValueError:
        print("Error: Please only enter a number!\n")
    else:
        break
while True:
    try:
        secondNum = float(input("\nPlease enter your second number: \n"))
    except ValueError:
        print("Error: Please only enter a number!\n")
    else:
        break
while True:
    try:
        thirdNum = float(input("\nPlease enter your third number: \n"))
    except ValueError:
        print("Error: Please only enter a number!\n")
    else:
        break

if thirdNum < firstNum > secondNum :
    print(f"\nThe largest number is {firstNum}")
elif thirdNum < secondNum > firstNum:
    print(f"\nThe largest number is {secondNum}")
else:
    print(f"\nThe largest number is {thirdNum}")
