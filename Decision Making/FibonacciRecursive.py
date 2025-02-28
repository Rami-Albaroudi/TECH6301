def fibonacci(term_input):
    if term_input == 0:
        return 0
    elif term_input == 1:
        return 1
    else:
        return fibonacci(term_input - 2) + fibonacci(term_input - 1)

term_input = int(input("Enter the number of terms: "))

print(f"Okay, I will print {term_input} terms of the Fibonacci sequence:")
    
for i in range(term_input):
    print(fibonacci(i))
