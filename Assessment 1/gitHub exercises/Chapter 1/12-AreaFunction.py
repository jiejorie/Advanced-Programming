# EXERCISE 12: AREA FUNCTION

def calculate_area(user_input):
    if user_input == 1:
        print("\nArea of a Square:")
        side = float(input("Enter a side length for your Square: "))
        area = side * side
        print(f"\nThe area of your Square is: {area:.2f}!")
    elif user_input == 2:
        print("\nArea of a Circle:")
        radius = float(input("Enter a radius for your Circle: "))
        area = 3.14 * radius**2
        print(f"\nThe area of your Circle is: {area:.2f}!")
    else:
        print("\nArea of a Triangle:")
        base = float(input("Enter the base of your Triangle: "))
        height = float(input("Enter the height of your Triangle: "))
        area = (base * height) / 2
        print(f"\nThe area of your Triangle is: {area:.2f}!")

def menu():
    print("1: Calculate the area of a square\n2: Calculate the area of a circle\n3: Calculate the area of a triangle ")
    user_input = int(input("\nWhat would you like to calculate?\nType '1', '2', or '3': "))
    return user_input

def main():
    print("Calculating the area")
    user_input = menu()
    calculate_area(user_input)


if __name__ == "__main__":
    main()
