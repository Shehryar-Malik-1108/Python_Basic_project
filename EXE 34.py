# QUESTION 34:

# Write a Python program to remove the nth index character from a nonempty string.

# ANSWER:

def remove_char(str1, n):

    first_part = str1[:n]
    last_part = str1[n + 1:]

    return first_part + last_part


print(remove_char('Python', 0))
print(remove_char('Pthon', 3))
print(remove_char('Python', 5))