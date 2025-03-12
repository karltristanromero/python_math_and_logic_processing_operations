# Prog01: Create a program that ask user to input 10 numbers. Display all 
# numbers that have duplicate.

# - set list that will store all the numerical inputs
# - for loop in range 10
# - input number
# - append number to list of all numerical inputs

# - set list of duplicate numbers
# - set list of num without duplicates

# - for loop in range of list of numerical inputs
# - if num not in num without duplicates
# - append num to list of num without duplicates
# - elif num in num without duplicates and num not in duplicate numbers
# - append num to list of duplicate numbers


# - print(duplicate numbers)


list_all_nums = []

for i in range(10):
    number = float(input(f"({i+1}) Enter a number: "))
    list_all_nums.append(number)

duplicate_num = []
num_without_duplicates = []

for num in list_all_nums:
    if num not in num_without_duplicates:
        num_without_duplicates.append(num)
    elif num in num_without_duplicates and num not in duplicate_num:
        duplicate_num.append(num)

print(f"The numbers with duplicates are: {duplicate_num}")
