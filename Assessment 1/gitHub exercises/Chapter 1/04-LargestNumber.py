# EXERCISE 4: LARGEST NUMBER
print("Checking for the Largest Number")
firstNum = float(input("\nPlease enter your first number: \n"))
secondNum = float(input("\nPlease enter your second number: \n"))
thirdNum = float(input("\nPlease enter your third number: \n"))

if firstNum > secondNum and firstNum > thirdNum:
    print(f"\nThe largest number is {firstNum}")
elif secondNum > firstNum and secondNum > thirdNum:
    print(f"\nThe largest number is {secondNum}")
else:
    print(f"\nThe largest number is {thirdNum}")
