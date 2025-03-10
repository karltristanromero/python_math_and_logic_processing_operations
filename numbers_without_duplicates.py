# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

'''
    set list of numbers
    for loop in range(10)
        input number
        if number in list of numbers
            pop the number from list of number
    print(list of numbers)


idea: use enumerate function and use the dictionary to store how many values were counted

'''
num_history = []
num_no_duplicates = []

for i in range(10):
    number = input(f"({i + 1}) Enter a number: ")

    if number in num_history:
        num_no_duplicates.remove(number)
    else:
        num_no_duplicates.append(number)
        num_history.append(number)

print(f"The numbers without duplicates are: {', '.join(num_history)}")