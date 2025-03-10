# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

'''

    input 2 numbers
    if number is smaller
        print number

'''

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if first_number < second_number:
    print(f"The number {first_number} is smaller than {second_number}.")
elif second_number < first_number:
    print(f"The number {second_number} is smaller than {first_number}.")