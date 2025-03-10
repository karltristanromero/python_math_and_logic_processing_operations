# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

'''
    set list of numbers
    for loop in range(10)
        input number
        if number in list of numbers
            pop the number from list of number
    print(list of numbers)

'''
list_of_numbers = []

for i in range(10):
    number = float(input(f"({i + 1}) Enter a number: "))
    if number in list_of_numbers:
        list_of_numbers.remove(number)
    else:
        list_of_numbers.append(number)



print(f"The numbers without duplicates are: {list_of_numbers}")