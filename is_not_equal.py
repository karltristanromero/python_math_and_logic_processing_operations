# Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

'''

    input 2 numbers
    if the numbers are not equal
        print "not equal"

'''

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if first_number != second_number:
    print(f"{first_number} and {second_number} are not equal.")