# QUESTION 13:

# Write a Python program to count the number 4 in a given list.

# ANSWER:

def list_count(nums):
    count = 0
    for n in nums:
        if n == 4:
            count = count + 1
    return count


print(list_count([4, 4, 4, 4, 4, 4, 4, 4, 4, 4]))
print(list_count([1, 4, 1, 4, 1, 4, 1, 4, 1, 4]))
