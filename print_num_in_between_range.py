# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
'''
    input for lower and upper boundaries of range
    for num between range of lower and upper boudnaries:
        print num
'''

lower_boundary = input("Enter a boundary: ")
upper_boundary = input("Enter a boundary: ")

lower_boundary = int(float(lower_boundary))
upper_boundary = int(float(upper_boundary))

if lower_boundary > upper_boundary:
    lower_boundary, upper_boundary = upper_boundary, lower_boundary

for num in range(lower_boundary + 1, upper_boundary):
    print(num, end=" ")