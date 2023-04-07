# QUESTION 4:

#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers. Go to the editor
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

# ANSWER:
values = input("Input some comma separated numbers:")
list = values.split(",")
tuple = tuple(list)
print("LIST: ",list)
print("TUPLE: ",tuple)