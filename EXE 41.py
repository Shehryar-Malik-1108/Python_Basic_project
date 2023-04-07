# QUESTION 41:

# Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

# ANSWER:

def to_upper_case(str1):
    num_upper = 0
    for letter in str1[:4]:
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper()
    return str1


print(to_upper_case("Python"))
print(to_upper_case("sHEhryar"))

