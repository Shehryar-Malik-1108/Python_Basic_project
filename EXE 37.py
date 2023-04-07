# QUESTION 37:

# Write a Python program to count the occurrences of each word in a given sentence.

# ANSWER:
def word_count(str1):
    counts = dict()
    words = str1.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_count('My name is Shehryar Malik and I am 18 years old.'))

