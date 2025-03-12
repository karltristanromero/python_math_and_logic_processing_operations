# Prog03: Create a program that ask user to input a number, continue asking 
# until the user input is invalid. Display the highest number

# - set highest_number to None

# - while loop
# - try-except
# - input number
# - if the highest_number is still set to None
# - replace highest number with the input number
# - elif input number is greater than highest number
# - replaca highest number with the input number
# - except a ValueError occurred
# - break the while loop 

# - print highest_number

# Main Program
highest_number = None

while True:
    try:
        number = float(input("Enter a number: "))

        if highest_number is None or number > highest_number:
            highest_number = number

    except ValueError:
        break

if highest_number is not None:
    print(f"The highest number you have entered is: {highest_number}")
else:
    print("There was no valid input entered.")