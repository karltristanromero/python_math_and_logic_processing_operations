# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. 
# Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when 
# the inputted number have duplicate.--is_unique_or_is_duplicate

'''
    set list_num
    while loop
        input number

        if number in list_num
            print duplicate
        elif not in list_num
            append number to list_num
            print unique
        else: 
            break loop

'''

list_numbers = []

while True:
    number = float(input("Enter a number: "))
    try:
        if number in list_numbers:
            print(f"{number} is a DUPLICATE!")
        else:
            list_numbers.append(number)
            print(f"{number} is UNIQUE!")
    except ValueError:
        break