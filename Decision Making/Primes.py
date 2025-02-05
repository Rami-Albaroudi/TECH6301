x = int(input("Enter a number: "))

sqrt = int(x ** (1/2))

for i in range(2, (x + 1)):
    is_prime = True
    for y in range(2, (int(i ** (1/2)) + 1)):
        if i % y == 0:
            is_prime = False
            break
    if is_prime == True:    
        print(i)
