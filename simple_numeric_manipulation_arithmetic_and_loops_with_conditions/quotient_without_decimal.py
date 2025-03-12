# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

# Pseudocode
# - input 2 numbers
# - divide the dividend to the divisor
# - print result without decimal

dividend = float(input("Enter the dividend: "))
divisor = float(input("Enter the divisor: "))

try:
    quotient = dividend / divisor
    print(f"{dividend} divided by {divisor} is {quotient:.0f}")
    
except ZeroDivisionError:
    print("You cannot divide by zero!")