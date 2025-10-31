# EXERCISE 13: PRODUCT OF LIST ITEMS
def multiply_list(numList):
    product = 1
    for num in numList:
        product = product * num
    return product

def main():
    print("Product of list items")
    numList = [2,3,4,6]
    product = multiply_list(numList)
    print(f"Product of values within the list: {product}")

if __name__ == "__main__":
    main()
