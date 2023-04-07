# QUESTION 23:

#Write a Python program to add two objects if both objects are integers.

# ANSWER:

def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Input must be an Integer"
    return a + b


print(add_numbers(10, 20))
print(add_numbers(2.2, 21))
print(add_numbers("2", 23))
print(add_numbers(20, 30))


