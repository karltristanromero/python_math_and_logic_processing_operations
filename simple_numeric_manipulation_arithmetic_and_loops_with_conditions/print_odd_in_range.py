# Prog08: Create a program that print all the odd numbers starting from 0 to 
# 100. (Use while loop)

# Pseudocode
# - set num
# - while num <= 100
# - if num is odd
# - print(num)
# - add + 1 to range_counter

num = 0

while num <= 100:
    if num % 2 != 0:
        print(num, end=" " )
    num += 1