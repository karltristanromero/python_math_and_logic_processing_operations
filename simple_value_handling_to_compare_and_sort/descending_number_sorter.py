# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
'''
    set list for all numerical inputs

    while loop
        try-except
            input number
            append number to list of numerical inputs
        excepy Value Error
            break the while loop
    
    sort the list
    print list
'''

list_of_all_nums = []

while True:
    try:
        number = float(input("Enter a number: "))
        list_of_all_nums.append(number)
    except ValueError:
        break

list_of_all_nums.sort(reverse=True)

print(f"I have sorted your numbers in descending order: {list_of_all_nums}")