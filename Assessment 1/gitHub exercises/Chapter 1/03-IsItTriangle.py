# EXERCISE 3: IS IT TRIANGLE
import random
print("Is it a triangle?")
side1 = float(input("\nEnter the first side of your triangle: \n"))
side2 = float(input("Enter the second side of your triangle: \n"))
side3 = float(input("Enter the third side of your triangle: \n"))

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
