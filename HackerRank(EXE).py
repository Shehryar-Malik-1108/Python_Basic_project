#EXE1:
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def car_max_speed(self):
#         print(self.max_speed)

#     def car_mileage(self):
#         print(self.mileage)

# modelX = Vehicle(240, 18)

# modelX.car_max_speed()
# modelX.car_mileage()

#EXE2

# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     def bus_name(self):
#         print(self.name)
#
#     def bus_max_speed(self):
#         print(self.max_speed)
#
#     def bus_mileage(self):
#         print(self.mileage)
# a = int(input("Enter Name"))
# b = int(input("Enter Speed"))
# c = int(input("Enter mileage"))
#
#
#
# School_bus.bus_name()
# School_bus.bus_max_speed()
# School_bus.bus_mileage()

#EXE3
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity=50)

# School_bus = Bus("School Volvo", 180, 12)

# print(School_bus.seating_capacity())

#EXE4
#
# class Vehicle:
#
#     def __init__(self,  color, name, max_speed, mileage):
#         self.color = color
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     pass
#
# class Car(Vehicle):
#     pass
#
# School_bus = Bus("White,","School Volvo,", 180, 12)
# print("Color:",School_bus.color,"Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
#
# car = Car("White,","Audi Q5,", 240, 18)
# print("Color:",car.color,"Name:",car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)


#EXE5
# class Vehicle:
#     def __init__(self, name, max_speed, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.max_speed = max_speed
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
# class Bus(Vehicle):
#     def fare(self):
#         amount = super().fare()
#         amount = amount + amount * 10 / 100
#         return amount
#
# School_bus = Bus("School Volvo",180, 12, 50)
# print("The final fare amount for the bus is :",School_bus.fare())


#EXE6
# def calculation(a, b,):
#     addition = a + b
#     subtraction = a - b
#     multiplication = a * b
#     division = a / b
#     # return multiple values separated by comma
#     return addition, subtraction, multiplication, division
#
# # get result in tuple format
# result= calculation(40, 10)
# print(result)

#EXE7
# Done by "RECURSION METHOD
# def addition(num):
#     if num:
#         return num + addition(num - 1)
#     else:
#         return 0
#
# result = addition(10)
# print(result)

#EXE8
#To find out evem numbers from list of 30 numbers by finding there range
# print(list(range(4,30,2)))

#EXE9
# #To find out the largest number in the list
# list = [2,3,4,5,6,67,7,58,92]
# print(max(list))

#EXE10

# # if __name__ == '__main__':
# #     n = int(input().strip())
# # if n%2!=0:
# #  print("Weird")
# # elif n%2==0 and n in range(2,6):
# #   print("Not Weird")
# # elif n%2 ==0 and n in range(6,21):
# #     print("Weird")
# # elif n%2==0 and n>20:
#     print("Not Weird")

#EXE11
# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#     if year % 400 == 0:
#         leap = True
#     elif year % 100 == 0:
#         leap = False
#     elif year % 4 == 0:
#         leap = True
#
#     return leap
#
# year = int(input())
# print(is_leap(year))

#EXE12

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# class Person1(Person):
#     def person_name(self):
#         print(self.name)
#
#     def person_age(self):
#         print(self.age)
#
# p1 = Person1("Shehryar",18)
# p1.person_name()
# p1.person_age()

#EXE 13
# thickness = int(input())
#
# c = 'H'
#
# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))
#
# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#EXE14
# def print_formatted(number):
#     l1 = len(bin(number)[2:])
#
#     for i in range(1, number + 1):
#         print(str(i).rjust(l1, ' '), end=" ")
#         print(oct(i)[2:].rjust(l1, ' '), end=" ")
#         print(((hex(i)[2:]).upper()).rjust(l1, ' '), end=" ")
#         print(bin(i)[2:].rjust(l1, ' '), end=" ")
#         print("")
#
#
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)


#EXE15
# if __name__ == '__main__':
#     s = input()
#
# res = False
# for i in s:
#     if i.isalnum():
#         res = True
#         break
# print(res)
#
# res = False
# for j in s:
#     if j.isalpha():
#         res = True
#         break
# print(res)
#
# res = False
# for k in s:
#     if k.isdigit():
#         res = True
#         break
# print(res)
#
# res = False
# for l in s:
#     if l.islower():
#         res = True
#         break
# print(res)
#
# res = False
# for l in s:
#     if l.isupper():
#         res = True
#         break
# print(res)

#EXE16
# N, M = map(int, input().split())
# for i in range(1, N, 2):
#     print(str('.|.' * i).center(M, '-'))
# print('WELCOME'.center(M, '-'))
# for i in range(N-2, -1, -2):
#     print(str('.|.' * i).center(M, '-'))

#EXE17
# N, X = input().split()
#
# io = list()
#
# for i in range(int(X)):
#     ip = map(float, input().split())
#     io.append(ip)
#
# for i in zip(*io):
#     print( sum(i)/len(i) )


#EXE18
# if __name__ == "__main__":
#     x, k = map(int, input().strip().split())
#     string = input().strip()
#
#     if eval(string) == k:
#         print(True)
#     else:
#         print(False)

#EXE19

# a = int(input())
# b = int(input())
# m = int(input())
# print(pow(a,b))
# print(pow(a,b,m))

#EXE20
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

#EXE 21:

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

#EXE 22:
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
#EXE 23:
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

#EXE 24:

# file1 = open("test.txt", "r")

# read_content = file1.read()
# print(read_content)

# file1.close()


#EXE 25:
# import calendar
# c = calendar.TextCalendar(firstweekday=6).formatyear(2023)
# print(c)

#EXE 26:
# import calendar
# c = calendar.TextCalendar(calendar.SUNDAY)
# a = c.formatmonth(2023,9)
# print(a)
# #

#EXE 25:
# class Nebulova:
#     def __init__(self,person1,person2,person3):
#         self.person1 = person1
#         self.person2 = person2
#         self.person3 = person3
#
#     def company_person1(self):
#         print(self.person1)
#
#     def company_person2(self):
#         print(self.person2)
#
#     def company_person3(self):
#         print(self.person3)
#
# company_nebulova = Nebulova("Ahmer" ,"Abdullah", "Shehryar")
# company_nebulova.company_person1()
# company_nebulova.company_person2()
# company_nebulova.company_person3()


#EXE 26:
# for i in range(1,int(input())):
#     print(int(i * 10**i / 9))


# #EXE 27:
# for i in range(1,int(input())+1):
#     print(((10**i-1)//9)**2)

#EXE 28:
# import math
# a = int(input())
# b = int(input())
#
# M = math.sqrt(a**2+b**2)
# theta = math.acos(b/M)
#
# print(int(round(math.degrees(theta),0)),"\u00B0",sep="")

#EXE 29:
# from random import randint
#
#
# t = ["Rock", "Paper", "Scissors"]
#
#
# computer = t[randint(0,2)]
#
#
# player = False
#
# while player == False:
#
#     player = input("Rock, Paper, Scissors?")
#     if player == computer:
#         print("Tie!")
#     elif player == "Rock":
#         if computer == "Paper":
#             print("You lose!", computer, "covers", player)
#         else:
#             print("You win!", player, "smashes", computer)
#     elif player == "Paper":
#         if computer == "Scissors":
#             print("You lose!", computer, "cut", player)
#         else:
#             print("You win!", player, "covers", computer)
#     elif player == "Scissors":
#         if computer == "Rock":
#             print("You lose...", computer, "smashes", player)
#         else:
#             print("You win!", player, "cut", computer)
#     else:
#         print("That's not a valid play.")
#
#     player = False
#     computer = t[randint(0,2)]

#EXE 30:
# import itertools
#
# a = input()
# b = int(a.split()[0])
# M = int(a.split()[1])
#
# N = []
# for i in range(b):
#   lst = input().split()
#   lst = [ int(n) for n in lst ]
#   lst = lst[1:]
#   N.append(lst)
#
# pro = list( itertools.product( *N ) )
#
# result = 0
# for item in pro:
#   sum=0
#   for num in item:
#     sum = sum +num**2
#   module = sum % M
#   if (module > result):
#     result = module
#
# print (result)


#EXE 31:
# from collections import namedtuple
#
# Student = namedtuple('Student', ['name', 'age', 'DOB'])
#
# S = Student('Nandini', '19', '2541997')
#
# print("The Student age using index is : ", end="")
# print(S[1])
#
# print("The Student name using keyname is : ", end="")
# print(S.name)

#EXE 32:
# from collections import Counter
#
# # With sequence of items
# print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B',
#                'B', 'A', 'C']))
#
# # with dictionary
# print(Counter({'A': 3, 'B': 5, 'C': 2}))
#
# # with keyword arguments
# print(Counter(A=3, B=5, C=2))

#EXE 33:
# from collections import OrderedDict
#
# print("This is a Dict:\n")
# d = {}
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
#
# for key, value in d.items():
#     print(key, value)
#
# print("\nThis is an Ordered Dict:\n")
# od = OrderedDict()
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# od['d'] = 4
#
# for key, value in od.items():
#     print(key, value)

#EXE 34:
# from collections import OrderedDict
#
# od = OrderedDict()
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# od['d'] = 4
#
# print('Before Deleting')
# for key, value in od.items():
#     print(key, value)
#
# # deleting element
# od.pop('a')
#
# # Re-inserting the same
# od['a'] = 1
#
# print('\nAfter re-inserting')
# for key, value in od.items():
#     print(key, value)

#EXE 35:
# from collections import defaultdict
#
# # Defining a dict
# d = defaultdict(list)
#
# for i in range(5):
#     d[i].append(i)
#
# print("Dictionary with values as list:")
# print(d)

#EXE 36:
# from collections import ChainMap
#
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# d3 = {'e': 5, 'f': 6}
#
# c = ChainMap(d1, d2, d3)
#
# print(c['a'])
#
# print(c.values())
#
# print(c.keys())

#EXE 36:
# import collections
#
# dic1 = {'a': 1, 'b': 2}
# dic2 = {'b': 3, 'c': 4}
# dic3 = {'f': 5}
#
# chain = collections.ChainMap(dic1, dic2)
#
# print("All the ChainMap contents are : ")
# print(chain)
#
# chain1 = chain.new_child(dic3)
#
# print("Displaying new ChainMap : ")
# print(chain1)

#EXE 37:

# from collections import deque
#
# de = deque([1, 2, 3])
#
# de.append(4)
#
# print("The deque after appending at right is : ")
# print(de)
#
# de.appendleft(6)
#
# print("The deque after appending at left is : ")
# print(de)

#EXE 38:
#
# from collections import deque
#
# de = deque([6, 1, 2, 3, 4])
#
# de.pop()
#
# print("The deque after deleting from right is : ")
# print(de)
#
# de.popleft()
#
# print("The deque after deleting from left is : ")
# print(de)

#EXE 39:
# import random
# number = random.randint(1, 10)
#
# player_name = input("Hello, What's your name?")
# number_of_guesses = 0
# print('Okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')
#
# while number_of_guesses < 5:
#     guess = int(input())
#     number_of_guesses += 1
#     if guess < number:
#         print('Your guess is little bit low')
#     if guess > number:
#         print('Your guess is little bit high')
#     if guess == number:
#         break
# if guess == number:
#     print('You "Won",WELL DONE!,'+ player_name)
#     print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
#
# else:
#     print('You lose! ,You did not guess the number, The number was ' + str(number))
# if guess != number:
#     print("New Game Starts!,"
#           "PRESS RUN BUTTON ON THE TOP")


#EXE 40:
# N = int(input())
# for i in range(1,10):
#     print(int(i*10**i/9))

#EXE 41:

# def remove(nums):
#     i = 0
#     for j in range(0, len(nums)):
#         if nums[j] != nums[i]:
#             i = i + 1
#             nums[i] = nums[j]
#     return i + 1
#
#
# nums = [0,0,1,1,1,2,2,3,3,4]
# steps = remove(nums)
# print(steps)
# print(nums[:steps])


# def maxCost(cost, labels, dailyCount):
#     # Write your code here
#     current_count = 0
#     total_cost = 0
#
#     cost_list = []
#
#     for c, l in zip(cost, labels):
#         if current_count == dailyCount:
#             cost_list.append(total_cost)
#             total_cost = 0
#             current_count = 0
#
#         if l == "legal" and current_count < dailyCount:
#             current_count += 1
#             total_cost += c
#         elif l == "illegal" and current_count < dailyCount:
#             total_cost += c
#
#     if current_count == dailyCount:
#         cost_list.append(total_cost)
#         total_cost = 0
#         current_count = 0
#
#     if len(cost_list) == 0:
#         return 0
#     else:
#         return max(cost_list)


#EXE 42:

# n = int(input())
# reverse = 0
# sign = -1 if n < 0 else 1
# n = abs(n)
#
# while n > 0:
#     a = n % 10
#     reverse = reverse * 10 + a
#     n = n // 10
#
# reverse = reverse * sign
# print(reverse)


#EXE 43:
# i = 1
# while i <= 10:
#     print(i * "·")
#     i += 1

#EXE 44:
# # by using for loop
#
# numbers = [1,2,3,4,5]
# for i in numbers:
#     print(i)
#
# # by using while loop
#
# i = 0
# while i <= len(numbers):
#     print(i)
#     i = i +1


#EXE 45:

# import pandas
#
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
#
# myvar = pandas.DataFrame(mydataset)
#
# print(myvar)

#EXE 46:
# import pandas as pd
#
# calories = {"day1": 420, "day2": 380, "day3": 390}
#
# myvar = pd.Series(calories)
#
# print(myvar)

#EXE 47:
# import pandas as pd
#
# calories = {"day1": 420, "day2": 380, "day3": 390}
#
# myvar = pd.Series(calories, index = ["day1", "day2"])
#
# print(myvar)

#EXE 48:
# import pandas as pd
#
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# myvar = pd.DataFrame(data)
#
# print(myvar)

#EXE 49:
# import pandas as pd
#
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
#
# # print(df)

#EXE 50:

# import json
#
# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
#
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# # print(y["age"])

#EXE 51:
# import json
#
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
#
# # use four indents to make it easier to read the result:
# print(json.dumps(x, indent=4))

#EXE 52:
# import json
#
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
#
# print(json.dumps(x, indent=4, separators=(". ", " = ")))

#EXE 53:
# import json
#
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
#
# # sort the result alphabetically by keys:
# print(json.dumps(x, indent=4, sort_keys=True))

#EXE 54:
# import pandas as pd
#
# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409.1,
#     "1":479.0,
#     "2":340.0,
#     "3":282.4,
#     "4":406.0,
#     "5":300.5
#   }
# }
#
# df = pd.DataFrame(data)
#
# print(df)

#EXE 55:
# import pandas as pd
#
# df = pd.read_csv('~/Downloads/data.csv')
#
# print(df.head(10))

#EXE 56:
# birth_year = input("Birth year: ")
# age = 2023 - int(birth_year)
# print(age)


#EXE 57:
# phone = input("Phone: ")
# digits_mapping = {
#     "1" : "One",
#     "2" : "Two",
#     "3" : "Three",
#     "4" : "Four"
# }
# output = ""
# for char in phone:
#     output += digits_mapping.get(char, "%") + " "
# print(output)

