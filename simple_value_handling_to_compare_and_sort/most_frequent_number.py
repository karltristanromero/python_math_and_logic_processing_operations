# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

'''
    set list of all numerical inputs
    
    while loop
        try-except
            input number
            append number to list of numerical inputs
        except Valueerror
            break the while loop

    def value counter that accepts (list, num_to_count) as input
        frequency = 0
        for index in list
            if number located in index is equal to number to be counted
                add 1 to frequency
        return frequency of number
        
    set all numerical input in dictionary 
    for num in list of numerical inputs
        place in a variable the return of value_counter(num)
        append num as key and return as value
    
    set a list for most frequent number to store all modes
    for mode, frequency enumerate the numerical input dictionary
        if list is empty
            initiate first mode as the number in list
        elif mode has greater frequency than the one in the list
            remove the one in the list
            append the mode
        elif mode has equal frequency with the one in the list
            append the mode

    print(list for most frequent numbers)
'''

list_of_all_nums = []

while True:
    try:
        number = float(input("Enter a number: "))
        list_of_all_nums.append(number)
    except ValueError:
        break

def number_counter(number_list: list, num_to_count: float) -> int:
    frequency = 0
    for num in number_list:
        if num == num_to_count:
            frequency += 1
    return frequency


numerical_input_dict = {}

for num in list_of_all_nums:
    frequency_count = number_counter(list_of_all_nums, num)
    numerical_input_dict[num] = frequency_count


most_frequent_num = []
num_dict_checker = {}

for mode, frequency in enumerate(numerical_input_dict): #returns mode as index

    if most_frequent_num == []:
        most_frequent_num.append(mode)
        num_dict_checker[mode] = frequency

    elif frequency > num_dict_checker[mode]: # Name Error, cannot access dictionary values, even when there are 2 or more values
        most_frequent_num = [mode]