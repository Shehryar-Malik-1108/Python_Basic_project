# QUESTION 20:

#Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero

# ANSWER:

def sum_of_three(x, y, z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z
    return sum


print(sum_of_three(2, 1, 2))
print(sum_of_three(1, 2, 3))
print(sum_of_three(6, 8, 6))
print(sum_of_three(5, 6, 9))

