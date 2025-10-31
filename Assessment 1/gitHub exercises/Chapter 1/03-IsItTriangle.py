# EXERCISE 3: IS IT TRIANGLE
import random
print("Is it a triangle?")
side1 = float(input("Enter the first side of your triangle: \n"))
side2 = float(input("Enter the second side of your triangle: \n"))
side3 = float(input("Enter the third side of your triangle: \n"))

answers = side1, side2, side3

def pick_side():
    side = random.choice(answers)
    answers.remove(side)
    return side

firstSide = pick_side()
secondSide = pick_side()
thirdSide = pick_side()

randomSides = firstSide, secondSide, thirdSide
duplicates = [item for item in randomSides if randomSides.count(item) >= 2]

if firstSide + secondSide >= thirdSide:
    print("\nThis is indeed a Triangle!")
    if len(duplicates) == 0:
        print("\nClassification:\n This Triangle is a Scalene.")
    elif len(duplicates) == 3:
        print("\nClassification:\n This Triangle is an Equilateral.")
    else:
        print("\nClassification:\n This Triangle is an Isosceles.") 
else:
    print("\nThis is unfortunately not a Triangle..")


