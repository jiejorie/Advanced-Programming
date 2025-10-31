# EXERCISE A: MULTIPLICATION TABLES
print("Multiplication Tables")
for multiplicand in range(1,11):
    print(f"\nMultiplication table of : {multiplicand}")
    for multiplier in range(1,11):
        print(f"{multiplicand} x {multiplier} = {multiplicand*multiplier}")
