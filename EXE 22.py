# QUESTION 22:

#Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

# ANSWER:

def test_number(x ,y):
    if x == y or (x-y) == 5 or (x + y) == 5:
        return True
    else:
         return False


print(test_number(7, 1))
print(test_number(10, 5))
