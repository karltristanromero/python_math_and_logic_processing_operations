# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

'''
    set a list of numerical inputs
    for loop in range 10
        input numbers
        if number not in list
            add number to list

    print list


'''

list_num_inputs = []

for i in range(10):
    num = input(f"({i+1}) Enter a number: ")
    if num not in list_num_inputs:

        list_num_inputs.append(num)

print(f"\nRemoving the duplicates you get: {', '.join(list_num_inputs)}")