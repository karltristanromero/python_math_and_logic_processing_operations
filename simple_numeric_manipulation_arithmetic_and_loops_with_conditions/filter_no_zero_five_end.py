# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

# - set num to 0
# - while loop in range 0-100
# - if num doesn't end in zero/five
# - print num
# - add + 1 to num

num = 0

while num < 101:
    if num % 5 != 0:
        print(num, end=" ")
    num += 1