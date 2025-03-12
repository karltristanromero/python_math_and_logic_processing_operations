# Prog06: Create a program that ask user to input 2 numbers. Print the result 
# when the first number is raised to the second number.

# Pseudocode
# - input 2 numbers
# - calculate the first_num raised to the second_num
# - print the result

first_number = float(input("Enter the base to be raised: "))
second_number = float(input("Enter the exponent: "))

result = first_number ** second_number

print(f"The result of raising {first_number} to {second_number} is {result}.")