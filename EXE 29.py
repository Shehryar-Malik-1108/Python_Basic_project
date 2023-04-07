# QUESTTION 29

# Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead. Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

# ANSWER:

def string_both_ends(str):
    if len(str) < 2:
        return ''

    return str[0:2] + str[-2:]


print(string_both_ends("w3resource"))
print(string_both_ends("w3"))
print(string_both_ends("w"))
