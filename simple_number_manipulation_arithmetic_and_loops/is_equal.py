# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" 
# when the numbers are the same.

# Pseudocode
# - input 2 numbers
# - if numbers are equal
# - print "equal"


first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if first_number == second_number:
    print(f"{first_number} and {second_number} are equal")