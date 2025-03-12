# Prog05: Create a program that ask user to input 2 numbers. Print the 
# remainder when the first number is divided by the second number.

# Pseudocode
# - input dividend and divisor
# - calculate remainder, use modulo
# - print remainder

dividend = float(input("Enter the dividend: "))
divisor = float(input("Enter the divisor: "))

try:
    remainder = dividend % divisor
    print(f"The remainder of {dividend} ÷ {divisor} is {remainder}")

except ZeroDivisionError:
    print("You cannot divide by zero!")