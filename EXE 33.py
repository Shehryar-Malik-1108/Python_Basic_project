# QUESTION 33:

# Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

# ANSWER:

def not_poor(str1):
    is_not = str1.find('not')
    is_poor = str1.find('poor')


    if is_poor > is_not and is_not > 0 and is_poor > 0 :
        str1 = str1.replace(str1[is_not:(is_poor + 4)],'good')
        return str1
    else:
        return str1


print(not_poor('The lyrics is not that poor'))
print((not_poor('The lyrics is poor')))

