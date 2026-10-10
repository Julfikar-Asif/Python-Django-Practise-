# class emni:
#     def __init__(me, name , age=18 ):
#         me.name = name 
#         me.age = age 
# p1= emni("asif")
# p2 =emni("jhboids", 27 )

# print(p1.name, p1.age)
# print(p2.name, p2.age)
# print(p1.__dict__)  
# print(p2.__dict__)  

# def bark(self):
#     print(self.name + " woof woof")


# bark(p1)
# bark(p2)

# class Person:
#   def __init__(self, name):
#     self.name = name

#   def printname(self):
#     print(self.name)

# p1 = Person("Tobias")
# p2 = Person("Linus")


# print(p1.name)


# # p1.printname()
# # p2.printname()

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def greet(self):
#     print("Hello, my name is " + self.name)

#   def introduce(self):
#     print("I am " + self.name + " and I am " + str(self.age) + " years old.")

# p1 = Person("Emil", 25)
# p2 = Person("Tobias", 30)
# p3 = Person("Linus", 35)
# p1.greet()
# p1.introduce()
# p2.greet()
# p2.introduce()
# p3.greet()
# p3.introduce()


# class Person:
#   def __init__(self, name):
#     self.name = name

#   def greet(self):
#     return "Hello, " + self.name

#   def welcome(self):
#     message = self.greet()
#     print(message + "! Welcome to our website.")

# p1 = Person("Tobias")
# p1.welcome()

for i in range(1, 6):
    print("*" * i)  #right triangle

for i in range(1,6):
    print(" " * (5 - i) + "*" * i)  #left triangle

row =6
for i in range(row):
    for j in range(row - i):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

