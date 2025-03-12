# Prog04: Create a program that ask user to input a number, continue asking 
# until the user input is invalid. Display the lowest number 
# --print_lowest_number

# Pseudocode
# - set lowest_number to None
# - while loop
# - try except
# - input num
# - if lowest_number is still None
# - set lowest_number into num's value
# - elif num is less than lowest_number
# - change lowest number's value with num's
# - except Value error
# - break

# - print(lowest_number)

# Main Program
lowest_number = None

while True:
    try:
        num = float(input("Enter a number: "))
        
        if lowest_number == None:
            lowest_number = num
        elif num < lowest_number:
            lowest_number = num

    except ValueError:
        break

print(f"The lowest number you have entered is: {lowest_number}")