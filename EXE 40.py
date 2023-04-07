# QUESTION 40:

# Write a Python function to reverse a string if its length is a multiple of 4

# ANSWER:

def reverse_string(str1):
    if len(str1) == 4:
        return ''.join((reversed(str1)))
    return str1


print(reverse_string("abcd"))
print(reverse_string('malik'))