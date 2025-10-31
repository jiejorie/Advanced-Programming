# EXERCISE 9: INTEGER LIST
print("Integer List")
intList = [5, 17, 13, 20, 6, 14, 9, 21, 10, 3]

print("\nValues within intList:")
for item in intList:
    print(f"{item} ", end="")

for item in intList:
    if item == max(intList):
        print(f"\n\nThe maximum value of intList is: {item}")
    elif item == min(intList):
        print(f"\nThe minimum value of intList is: {item}")
    else:
        continue

print("\n\nPrint intList values in ascending order:")
ascending = sorted(intList)
for item in ascending:
    print(f"{item} ", end="")

print("\n\nPrint intList values in descending order:")
descending = sorted(intList, reverse=True)
for item in descending:
    print(f"{item} ", end="")

print("\n\nAppending two values into intList:")
intList.append(8)
intList.append(7)
for item in intList:
    print(f"{item} ", end="")
