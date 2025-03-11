# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

'''
    set list of numbers
    for loop in range(10)
        input number
        if number in list of numbers
            pop the number from list of number
    print(list of numbers)

'''
list_of_num = []

for i in range(10):
    num_input = input(f"({i + 1}) Enter a number: ")
    list_of_num.append(num_input)

num_without_dupli = []
duplicates = []

for num in list_of_num:

    if num not in num_without_dupli and num not in duplicates:
        num_without_dupli.append(num)

    elif num in num_without_dupli:
        num_without_dupli.remove(num)
        duplicates.append(num)


print(f"The numbers without duplicates are: {' '.join(num_without_dupli)}")