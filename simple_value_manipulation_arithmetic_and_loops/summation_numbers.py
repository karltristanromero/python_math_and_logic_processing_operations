# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

'''
    set sum container
    for loop with range of 10
        input number
        add number to sum

'''

sum = 0

for i in range(10):
    addend = float(input(f"({i + 1}) Enter an addend: "))
    sum += addend

print(f"Summing it all up, you get: {sum}!!")