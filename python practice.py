# (Mosh Hamedani Exercises):

#EXE 1:(Write a function that returns the maximum of two numbers.)
# def maximum(a,b):
#     if a > b:
#         print(a,"is the biggest number")
#     else:
#         print(b,"is the biggest number")
# maximum(10,9)
#

#EXE 2:(Write a function called fizz_buzz that takes a number.
    #1: If the number is divisible by 3, it should return “Fizz”.
    #2: If it is divisible by 5, it should return “Buzz”.
    #3: If it is divisible by both 3 and 5, it should return “FizzBuzz”.
    #4: Otherwise, it should return the same number.)

# def fizz_buzz(number):
#     num = number
#     if num % 3 == 0 and num % 5 == 0 :
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)
# fizz_buzz(3)

#EXE 3:(Write a function for checking the speed of drivers. This function should have one parameter: speed.

        #1: If speed is less than 70, it should print “Ok”.
        #2: Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
        #3: If the driver gets more than 12 points, the function should print: “License suspended”
# )
#
# def Speed_Limit(speed):
#     if speed == 80:
#         print("Speed is too much")
#     elif speed < 70:
#         print("OK")
#
# Speed_Limit(60)

#EXE 4:(Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
    # 0 EVEN
    # 1 ODD
    # 2 EVEN
    # 3 ODD  )

# def showNumbers(num):
#         if num % 2 == 0:
#             print("Even")
#         elif num % 3 == 0:
#             print("Odd")
#
# showNumbers(2)


#EXE 5:(Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.)
# def num(limit):
#     sum = 0
#     for i in range(0,limit+1):
#         if i % 3 == 0 or i % 5 == 0:
#             sum += 1
#             print(sum)
# num(20)

#EXE 6:Write a function called show_stars(rows). If rows is 5, it should print the following:

    # *
    # **
    # ***
    # ****
    # *****

# i = 1
# while i <= 5:
#     print(i * "*")
#     i += 1


#EXE 7:(Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.)

# def prime(num):
#     if num == 1 or num == 0:
#         print(num, "is neither prime or composite")
#         for i in range(2, num+1):
#             if num % i == 0:
#                 print(num, "is not a prime number")
#                 break
#             else:
#                 print(num, "is a prime number")
#                 break
# prime(15)

#
# temperature = int(input("Enter any temparature: "))
#
# if temperature > 30:
#     print("It's a hot day")
# elif temperature < 10:
#     print("It's a cold day")
# else:
#     print("It's neither hot nor cold")


# name = input("Enter any name: ")
#
# if len(name) < 3:
#     print("Name must be at least of 3 characters")
# elif len(name) >= 50:
#     print("Name can maximum be of 50 characters")
# else:
#     print("Name looks good!")


# num = int(input("Enter any number: "))
# while num <= 10:
#     print(num)
#     num = num + 1
# print("Done!")


# numbers = [1, 1, 1, 1, 8]
#
# for x_count in numbers:
#     print('x' * x_count)
