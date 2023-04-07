# EXE 1: (ITERATORS)
import calendar

# my_list = [4, 7, 6, 9]
# iterator = iter(my_list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# EXE 2:

# my_list = [4, 7, 0]
# for i in my_list:
# print(i)

# EXE 3:


# my_list = [1, 2, 3, 4, 5]
# iterator = iter(my_list)
# for i in iterator:
#     print(i)


# EXE 4:
# class PowTwo:
#
#     def __init__(self, max=0):
#         self.max = max
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
# numbers = PowTwo(4)
# i = iter(numbers)
#
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# EXE 5:
# ITERATOR CODE EXAMPLE:
# class Even:
#     def __init__(self,max):
#         self.n = 2
#         self.max = max
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n <= self.max:
#             result = self.n
#             self.n += 2
#             return result
#         else:
#             raise StopIteration
#
#
# numbers = Even(12)
#
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

# EXE 6:
#   GENERATOR CODE EXAMPLE:

# def even_generator(max):
#     n = 2
#     while n <= max:
#         yield n
#         n += 2
#
#
# numbers = even_generator(12)
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
#

#     name = "John"
#     return lambda: "Hi " + name
#
#
# message = greet()
# print(message())

#EXE 8:
# def calculate():
#     num = 1
#
#     def inner_func():
#         nonlocal num
#         num += 2
#         return num
#     return inner_func
#
#
# odd = calculate()
#
#
# print(odd())
# print(odd())
# print(odd())
#
# odd2 = calculate()
# print(odd2())


#EXE 9:
# def make_multiplier_of(n):
#     def multiplier(x):
#         return x * n
#     return multiplier
#
#
# times3 = make_multiplier_of(3)
# times5 = make_multiplier_of(5)
# times6 = make_multiplier_of(6)
# times9 = make_multiplier_of(9)
#
# print(times3(9))
# print(times5(3))
# print(times5(times3(2)))
# print(times6(6))
# print(times9(9))

#EXE 10:
# def fibonacci_numbers(nums):
#     x, y = 0, 1
#     for _ in range(nums):
#         x, y = y, x+y
#         yield x
#
#
# def square(nums):
#     for num in nums:
#         yield num**2
#
#
# print(sum(square(fibonacci_numbers(20))))

#EXE 11:
# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
#
#
# def ordinary():
#     print("I am ordinary")
#
# decorated_func = make_pretty(ordinary)


# decorated_func()

#EXE 12:
# def make_pretty(func):
#
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
#
# @make_pretty
# def ordinary():
#     print("I am ordinary")
#
# ordinary()

#EXE 13:
# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Oh nooooo! cannot divide")
#             return
#
#         return func(a, b)
#     return inner
#
#
# @smart_divide
# def divide(a, b):
#     print(a/b)
#
# divide(2,5)
# divide(2,0)

#EXE 14:
# def dollar(func):
#     def inner(*s, **n):
#         print("$" * 100)
#         func(*s, **n)
#         print("$" * 100)
#     return inner
#
#
# def arrows(func):
#     def inner(*s, **n):
#         print("^" * 100)
#         func(*s, **n)
#         print("^" * 100)
#     return inner
#
#
# @dollar
# @arrows
# def printer(msg):
#     print(msg)
#
# printer("                 Helloooooooooooooooooooooooooooooooooooooooooooooooooooo!")


#EXE 15:
# class Celsius:
#     def __init__(self, temperature=0):
#         self.temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32
#
#
# human = Celsius()
#
# human.temperature = 37
# print(human.temperature)
# print(human.to_fahrenheit())

#EXE 16:
# class Celsius:
#
#     def __init__(self, temperature):
#         self.temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8)+32
#
#
# human = Celsius(0)
#
#
# human.temperature = 37
# print(human.temperature)
# print(human.to_fahrenheit())

#EXE 17:
# class Celsius:
#     def __init__(self, temperature=0):
#         self.set_temperature(temperature)
#
#     def to_fahrenheit(self):
#         return (self.get_temperature() * 1.8) + 32
#
#     # getter method
#     def get_temperature(self):
#         return self._temperature
#
#     # setter method
#     def set_temperature(self, value):
#         if value < -273.15:
#             raise ValueError("Temperature below -273.15 is not possible.")
#         self._temperature = value
#
#
# human = Celsius(37)
#
# print(human.get_temperature())
#
# print(human.to_fahrenheit())
#
# human.set_temperature(-300)
#
# print(human.to_fahrenheit())

#EXE 18:
# import re
#
# pattern = '^a...s$'
# test_string = 'abyss'
# result = re.match(pattern, test_string)
#
# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")

#EXE 19:

# import re
#
# string = 'Twelve:12 Eighty nine:89.'
# pattern = '\d+'
#
# result = re.split(pattern, string)
# print(result)

#EXE 20:
# import re
# string = "abc 12\
# de 23 \n f45 6"
# pattern = '\d+'
# a = ""
#
# new_string = re.sub(pattern, a, string)
# print(new_string)


#EXE 21:
# import re
# string = "hello 1 sherry 10 how are you 20"
# pattern = "\d+"
# result = re.findall(pattern,string)
# print(result)

#EXE 22:
# import re
# string = "Sherry:18 Shani:13"
# pattern = "\d+"
# result = re.split(pattern,string)
# print(result)

#EXE 23:
# import re
# string = "abc 12 de 34 f45 9"
# pattern = "\s+"
# replace = ""
# result = re.sub(pattern,replace,string)
# print(result)

#EXE 24:
# import re
# string = "abc 12 de 34 f45 9"
# pattern = "\s+"
# replace = ""
# result = re.subn(pattern,replace,string)
# print(result)


#EXE 25:
# import re
# string = "Python is fun"
# match = re.search("\APython",string)
# if match:
#     print("pattern found inside the string")
# else :
#     print("pattern not found inside the string")

#EXE 26:
# import re
# string = "Python is fun"
# pattern = "\A"
# match = re.search(pattern,string)
# print(match)

#EXE 27:
# import re
# string = "37405 234,2101 1111"
# pattern = "(\d{3})(\d{2})"
# match = re.search(pattern,string)
# if match:
#     print(match.group())
# else:
#     print("pattern not found inside the string")

#EXE 28:
# import re
# string = "\n and \r are escape sequences"
# pattern = r"[\n\r]"
# result = re.findall(pattern,string)
# print(result)

#EXE 29:
# import datetime as dt
# current_date = dt.datetime.today()
# print(current_date)

#EXE 30:
# import datetime as dt
# date1 = dt.date.today()
# print(date1)
# print("Year:",date1.year)
# print("Month:",date1.month)
# print("Day:",date1.day)

#EXE 31:
# import datetime as dt
# time_1 = dt.time(10,45,35)
# print(time_1)
# print("Hour:",time_1.hour)
# print("Minute:",time_1.minute)
# print("Second:",time_1.second)

#EXE 32:
# import datetime as dt
# current_datetime = dt.datetime.now()
# print(current_datetime)

#EXE 33:
# import datetime as dt
# current_time = dt.datetime.now()
# next_new_year = dt.datetime(2024,1,1)
# remaining_time = next_new_year - current_time
# print(remaining_time)

#EXE 34:
#
# from datetime import datetime
#
# now = datetime.now()
#
# year = now.strftime("%Y")
# print("year:", year)
#
# month = now.strftime("%m")
# print("month:", month)
#
# day = now.strftime("%d")
# print("day:", day)
#
# time = now.strftime("%H:%M:%S")
# print("time:", time)
#
# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("date and time:",date_time)

#EXE 35:
# from datetime import datetime
#
# # timestamp is number of seconds since 1970-01-01
# timestamp = 1545730073
#
# # convert the timestamp to a datetime object in the local timezone
# dt_object = datetime.fromtimestamp(timestamp)
#
# # print the datetime object and its type
# print("dt_object =", dt_object)
# print("type(dt_object) =", type(dt_object))
#
#EXE 36:
# from datetime import datetime
# now = datetime.now()
# ts = datetime.timestamp(now)
# print("timestamp:",ts)

#EXE 37:
# import time
#
# result = time.localtime(1672214933)
# print("result:", result)
# print("\nyear:", result.tm_year)
# print("tm_hour:", result.tm_hour)

#EXE 38:
# import time
#
# result = time.gmtime(123456789)
# print("result:", result)
# print("\nyear:", result.tm_year)
# print("tm_hour:", result.tm_hour)
# print("tm_minutes:",result.tm_min)

#EXE 39:
# import time
#
# while True:
#     localtime = time.localtime()
#     result = time.strftime("%I:%M:%S %p", localtime)
#     print(result)
#     time.sleep(1)

#EXE 40:
# import calendar
# c = calendar.TextCalendar(calendar.SUNDAY)
# a = c.formatmonth(2023,9)
# print(a)

#EXE 41:
# import calendar
# c = calendar.TextCalendar(firstweekday=6).formatyear(2023)
# print(c)

# EXE 42:

# file1 = open("test.txt", "r")

# read_content = file1.read()
# print(read_content)

# file1.close()

#EXE 43:
# import re
#
# a = int(input())
# for i in range(a):
#     try:
#         re.compile(input())
#         Output = True
#     except re.error:
#         Output = False
#
#     print(Output)

#EXE 44:
# from itertools import combinations
# a = int(input())
# b = input().split()
# c = int(input())
#
# length = len(list(combinations(b,c)))
# data = 0
# for i in combinations(b,c):
#     if "a" in i:
#         data = data + 1
# print(float("{:12}".format(data/length)))
#

#EXE 45:
# import math
#
# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary
#
#     def __add__(self, no):
#         return Complex(self.real + no.real, self.imaginary + no.imaginary)
#
#     def __sub__(self, no):
#         return Complex(self.real - no.real, self.imaginary - no.imaginary)
#
#     def __mul__(self, no):
#         prod = complex(self.real, self.imaginary) * complex(no.real, no.imaginary)
#         return Complex(prod.real, prod.imag)
#
#     def __truediv__(self, no):
#         div = complex(self.real, self.imaginary) / complex(no.real, no.imaginary)
#         return Complex(div.real, div.imag)
#
#     def mod(self):
#         m = math.sqrt(self.real ** 2 + self.imaginary ** 2)
#         return Complex(m, 0)
#
#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result
#
#
# if __name__ == '__main__':
#     c = map(float, input().split())
#     d = map(float, input().split())
#     x = Complex(*c)
#     y = Complex(*d)
#     print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')

#EXE 46:
# def wrapper(f):
#     def fun(l):
#         f(["+92" + c[-1:-5] + " " + c[-10:] for c in l])
#     return fun
#
# @wrapper
# def sort_phone(l):
#     print(*sorted(l), sep='\n')
#
# if __name__ == '__main__':
#     l = [input() for i in range(int(input()))]
#     sort_phone(l)
#



