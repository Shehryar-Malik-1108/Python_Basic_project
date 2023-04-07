# QUESTION 14:

#Write a Python program to test whether a passed letter is a vowel or not

# ANSWER:

def is_vowel(characters):
    all_vowels = "aeiou"
    return characters in all_vowels


print(is_vowel("s"))
print(is_vowel("i"))