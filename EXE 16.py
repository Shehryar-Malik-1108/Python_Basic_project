# QUESTION 16:

#Write a Python program to create a histogram from a given list of integers

# ANSWER:

def histogram( items ):
    for n in items:
        output = ''
        times = n
        while (times > 0):
            output += '*'
            times = times - 1
        print(output)


histogram([1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

