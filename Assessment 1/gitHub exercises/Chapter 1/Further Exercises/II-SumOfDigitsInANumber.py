# EXERCISE II: SUM OF DIGITS IN A NUMBER
print("Sum of Digits within a Number")
number = input("\nEnter a number with more than 1 digit to calulate the sum of each number: ")
number_list = []
for digit in number:
    digit = int(digit)
    number_list.append(digit)
total = sum(number_list)
print(f"\nThe sum of each digit within {number} is {total}!")