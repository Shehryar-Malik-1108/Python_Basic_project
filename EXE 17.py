# QUESTION 17:

# Write a Python program that concatenates all elements in a list into a string and returns it.

# ANSWER:

def concatenate_list_data( list ):
    result = ''
    for element in list:
        result += str(element)
    return result


print(concatenate_list_data([1, 2, 3, 4, 5, 6, 7, 8, 9]))