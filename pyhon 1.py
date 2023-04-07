#EXAMPLE 1:

# class Parrot:
#
#     name = ""
#     age = 0
#
# parrot1 = Parrot()
# parrot1.name = "Blu"
# parrot1.age = 10
#
# parrot2 = Parrot()
# parrot2.name = "Woo"
# parrot2.age = 15
#
# print(f"{parrot1.name} is {parrot1.age} years old")
# print(f"{parrot2.name} is {parrot2.age} years old")

#EXAMPLE 2:
# class Animal:
#     name = ""
#     def eat(self):
#         print("I can eat")
#
# class Dog(Animal):
#     def display(self):
#         print("My name is ", self.name)
#
# labrador = Dog()
#
# labrador.name = "Rohu"
# labrador.eat()
# labrador.display()

#EXAMPLE 3
# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
#
#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
#
#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])

#EXAMPLE 4
# class Mammal:
#     def mammal_info(self):
#         print("Mammals can give direct birth.")
#
# class WingedAnimal:
#     def winged_animal_info(self):
#         print("Winged animals can flap.")
#
# class Bat(Mammal, WingedAnimal):
#     pass
#
# b1 = Bat()
#
# b1.mammal_info()
# b1.winged_animal_info()

#EXAMPLE 5
# class Computer:
#
#     def __init__(self):
#         self.__maxprice = 500
#
#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))
#
#     def setMaxPrice(self, price):
#         self.__maxprice = price
#
# c = Computer()
# c.sell()

# c.__maxprice = 1000
# c.sell()

# c.setMaxPrice(1000)
# c.sell()

#EXAMLE 6
# class Vehicle:
#      def __init__(self, name , color):
#          self.name = name
#          self.color = color
# class car(Vehicle):
#      def get(self):
#          print(self.name)
#          print(self.color)
# class bike(Vehicle):
#     def info(self):
#         print(self.name)
#         print(self.color)
#
# #object for car
# car1=car("Coure","BLue")
# car1.get()
#
# #object for bike
# bike1= bike("Cafe Racer","Black")
# bike1.info()


#EXAMPLE 7
# class Calculator:
#     def __init__(self):
#         self.a = []
#         for i in range(0, 5):
#             self.a.append(int(input("Enter any list of integers")))
#
#     def add(self):
#         sum = 0
#         for i in self.a:
#             sum = sum + i
#         print("sum = ", sum)
#
#     def sub(self):
#         sub = 100
#         for i in self.a:
#             sub = sub - i
#         print("sub = ", sub)
#
#     def mul(self):
#         mul = 5
#         for i in self.a:
#             mul = mul * i
#         print("mul = ", mul)
#
#     def div(self):
#         div = 10
#         for i in self.a:
#             div = div / i
#         print("div = ", div)
# c = Calculator()
# c.add()
# c.sub()
# c.mul()
# c.div()



