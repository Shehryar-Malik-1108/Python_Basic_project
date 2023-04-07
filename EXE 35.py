# QUESTION 35:

# Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.

# ANSWER:

def exchange_string(str1):

    return str1[-1:] + str1[1:-1] + str1[:1]


print(exchange_string('abcd'))
print(exchange_string('12345'))