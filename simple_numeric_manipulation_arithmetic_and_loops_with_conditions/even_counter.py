# Prog07: Create a program that ask user to input 10 numbers. Print how many 
# are even numbers.

# Pseudocode
# - set even counter
# - for loop in range 10
# - if even
# - add 1 to even
# - print even counter

even_counter = 0

for i in range(10):
    num = float(input("Enter a number: "))
    if num % 2 == 0:
        even_counter += 1

print(f"There are {even_counter} even numbers")