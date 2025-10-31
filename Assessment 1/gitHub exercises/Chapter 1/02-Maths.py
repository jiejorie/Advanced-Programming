# EXERCISE 2 : MATHS
print("Maths")
while True:
    try:
        value1 = float(input("\nEnter your first value: \n"))
    except ValueError:
     print("Error: Please only enter a number\n")
    else:
       break
while True:
    try:
        value2 = float(input("Enter your second value: \n"))
    except ValueError:
     print("Error: Please only enter a number\n")
    else:
       break
sum = value1 + value2
diff = value1 - value2
product = value1 * value2
quotient = value1 / value2
remainder = value1 % value2
print(f"\nSum: {sum}\nDifference: {diff}\nProduct: {product}\nQuotient: {quotient}\nRemainder: {remainder}")
