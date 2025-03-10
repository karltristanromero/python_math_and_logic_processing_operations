# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
'''
    input for lower and upper boundaries of range
    for num between range of lower and upper boudnaries:
        print num
'''

lower_boundary = int(input("Enter the lower boundary: "))
upper_boundary = int(input("Enter the upper boundary: "))

for num in range(lower_boundary + 1, upper_boundary):
    print(num, end=" ")