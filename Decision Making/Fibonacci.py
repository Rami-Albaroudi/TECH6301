term_input = int(input("Enter a number of terms: "))

print(f"Okay, I will print {term_input} terms of the Fibonnaci sequence.")

counter = 0

while counter != term_input:
    if counter == 0:
        result = 0
        counter += 1
    elif counter == 1:
        second_number = 1
        result = second_number
        counter += 1
    else: 
        first_number = second_number
        second_number = result
        result = second_number + first_number
        counter += 1

print(result)