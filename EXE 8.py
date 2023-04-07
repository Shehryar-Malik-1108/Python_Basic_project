# QUESTION 8:

#Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.

# ANSWER:
import calendar

year = int(input("Enter any Year: "))
month = int(input("Enter any Month: "))

print(calendar.month(year,month))