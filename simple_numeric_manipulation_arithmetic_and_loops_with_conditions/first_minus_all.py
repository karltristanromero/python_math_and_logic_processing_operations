# Prog06: Create a program that ask user to input 10 numbers. Print the result 
# of the first number minus all of the remaining numbers.

# Pseudocode
# - set difference
# - for loop in range 10
# - input number
# - if first input
# - add to difference
# - else
# - subtract to diff


difference = 0

for i in range(10):
    num = float(input("Enter a number: "))
    if i == 0:
        difference += num
    else:
        difference -= num

print(f"The difference of all numbers to the first input is: {difference}")