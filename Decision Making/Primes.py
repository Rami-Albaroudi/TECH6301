x = int(input("Enter a number: "))

prime = True
sqrt = int(x ** (1/2))

if x == 2:
    pass
elif x < 2:
    prime = False
else:
    for i in range(2, (sqrt + 1)):
        if x % i == 0:
            prime = False
            break
 
print(prime)
