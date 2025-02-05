def calculateFactorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        product = x * calculateFactorial(x-1)
        return product
    
x = int(input("Enter a number to calculate the factorial for: "))
print(f"{calculateFactorial(x)}")