# EXERCISE 3: IS IT TRIANGLE
print("Is it a triangle?")
while True:
    try:
        side1 = float(input("\nEnter the first side of your triangle: \n"))
    except ValueError:
        print("Error: Please only enter a number!\n")
    else:
        break
while True:
    try:
        side2 = float(input("Enter the second side of your triangle: \n"))
    except ValueError:
        print("Error: Please only enter a number!\n")
    else:
        break
while True:
    try:
        side3 = float(input("Enter the third side of your triangle: \n"))
    except ValueError:
        print("Error: Please only enter a number!\n")
    else:
        break

if side1 + side2 >= side3 or side2 + side3 >= side1 or side1 + side3 >= side2:
    print("\nThis is indeed a Triangle!")
    if side1 == side2 == side3:
        print("\nClassification:\n This Triangle is an Equilateral.")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("\nClassification:\n This Triangle is an Isosceles.") 
    else:
        print("\nClassification:\n This Triangle is a Scalene.")
else:
    print("\nThis is unfortunately not a Triangle..")
