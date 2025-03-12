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
    
    set list of most frequent numbers
    set dictionary as num_dict_value 

    for loop the dictionary's numerical input using items() to return key-value
        if most frequent numbers is empty
            add the key to list of most freq numbers
            add key-value pair in num_dict_value
        elif value > greater than the value in num_dict_value
            change list into the current key
            change dictionary into current key-value pair

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