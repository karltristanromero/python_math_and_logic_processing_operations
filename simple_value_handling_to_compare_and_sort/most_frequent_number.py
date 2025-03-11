# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

'''
    set list of all numerical inputs
    
    while loop
        try-except
            input number
            append number to list of numerical inputs
        except Valueerror
            break the while loop

    def value counter that accepts (index) as input
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