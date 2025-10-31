# EXERCISE C: CALCULATOR FUNCTION
print("Calculator Function")

def menu():
    while True:
        print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus")
        try:
            menuPick = int(input("\nPick an operation you would like to calculate with\nType your option's corresponding number: "))
        except ValueError:
            input("\nPlease only enter a number")
        else:
            if 1 <= menuPick <= 5:
                break
            else:
                input("\nPlease only enter a number between 1 and 5")
    return menuPick

def calculate(menuPick):
    while True:
        try: 
            value1 = float(input("\nEnter your first value: "))
        except ValueError:
            print("Please only enter digits")
        else:
            break
    while True:
        try: 
            value2 = float(input("Enter your second value: "))
        except ValueError:
            print("Please only enter digits")
        else:
            break
    if menuPick == 1:
        return value1 + value2
    elif menuPick == 2:
        return value1 - value2
    elif menuPick == 3:
        return value1 * value2
    elif menuPick == 4:
        return value1 / value2
    else:
        return value1 % value2

def main(): 
    again = ""
    while again != "n":
        menuPick = menu()
        answer = calculate(menuPick)
        print(f"\nThe answer of this equation is: {answer:.2f}")
        while True:
            again = input("\nPerform another operation? (y/n): ").lower()
            if again == "n":
                print("Thank you for using Calculator!")
                break
            elif again == "y":
                break
            else:
                print("Enter only 'y' or 'n'.")
                continue

if __name__ == "__main__":
    main()
