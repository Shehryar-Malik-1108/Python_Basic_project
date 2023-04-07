# QUESTION 39:

# Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically). Go to the editor
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

# ANSWER:

items = input("Enter any comma separated sequence of words: ")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))