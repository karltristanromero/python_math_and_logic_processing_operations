# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number --print_lowest_number
'''
    set lowest_number to None
    while loop
        input num
        try-except
            if num is still None
                set lowest_number into num's value
            elif num is less than lowest_number
                change lowest number's value with num's
        except Value error
            break
            
    print(lowest_number)

'''

lowest_number = None