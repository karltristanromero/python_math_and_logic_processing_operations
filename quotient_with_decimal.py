# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

'''
    input 2 numbers
    divide the first to the second number
    print the quotient with decimal

'''
dividend = float(input("Enter the dividend: "))
divisor = float(input("Enter the divisor: "))

quotient = dividend / divisor

print(f"The quotient of {dividend} ÷ {divisor} is {quotient}")