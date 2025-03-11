# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
'''
    set list that will store all the numerical inputs
    set list for duplicate numbers
    for loop in range 10
        input number
        if number is not found in list of numerical inputs
            append number to list of numerical inputs
        elif number is found in list of numerical inputs
            append to duplicate numbers
    
    print(duplicate numbers)

'''

list_all_num = []
duplicate_num = []

for i in range(10):
    number = float(input(f"({i+1}) Enter a number: "))
    if number not in list_all_num:
        list_all_num.append(number)
    else:
        duplicate_num.append(number)

print(duplicate_num)
