# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

'''
    set odd_counter
    for loop
        input number
        if odd (use modulo)
            add 1 to odd_counter
'''

odd_counter = 0

for i in range(10):
    num = float(input(f"({i+1}) Enter a number: "))
    if num % 2 != 0:
        odd_counter += 1

print(f"There are {odd_counter} odd numbers.")