# Prog01: Create a program that ask user to input 2 numbers. Print the bigger 
# number.

# Pseudocode
# - input 2 numbers
# - if number is greater than the other
# - print result    

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if first_number > second_number:
    print(f"The number {first_number} is bigger than {second_number}.")
    
elif second_number > first_number:
    print(f"The number {second_number} is bigger than {first_number}.")