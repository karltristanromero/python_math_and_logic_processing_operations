# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

'''
    set list of all numerical inputs
    
    while loop
        try-except
            input number
            append number to list of numerical inputs
        except Valueerror
            break the while loop

            
    set dictionary to count frequency of each numerical input
    for loop the list of numerical inputs
        if the number is already in numerical inputs
            add 1 to the value 
        else
            set the num with a frequency of 1
    
    set list for most_frequent_numbers
    set 0 to highest_freq for comparison
    
    for loop the dictionary using items() and return the number and frequency
        if the highest_freq is still set to 0 or frequency > highest_freq
            update most frequent numbers into the current num(key)
            update the highest freq to the current frequency(value)
        elif frequency is = to highest_Freq value
            append the number to most_frequent_numbers  
    
    print most_frequent_numbers

'''

list_of_all_nums = []

while True:
    try:
        number = float(input("Enter a number: "))
        list_of_all_nums.append(number)
    except ValueError:
        break


