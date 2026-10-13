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

# for i in range(1, 6):
#     print("*" * i)  #right triangle

# for i in range(1,6):
#     print(" " * (5 - i) + "*" * i)  #left triangle

# row =6
# for i in range(row):
#     for j in range(row - i):
#         print(" ", end="")
#     for k in range(2 * i + 1):
#         print("*", end="")
#     print()

class Employee:

    raise_amount = 1.04
    def __init__(self, fisrt, last,pay):
        self.fisrt = fisrt
        self.last = last
        self.pay = pay
        self.email = fisrt  + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.fisrt, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
    
    # @classmethod
    # def from_string(cls, emp_str):
    #     first, last, pay = emp_str.split("-")
    #     return cls(first, last, pay)

    # @staticmethod
    # def is_workday(day):
    #     if day.weekday() == 5 or day.weekday() == 6:
    #         return False
    #     return True

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, fisrt, last, pay, prog_lang):
        super().__init__(fisrt, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, fisrt, last, pay, employees=None):
            super().__init__(fisrt, last, pay)
            if employees is None:
                self.employees = []
            else:
                self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())




# dev_1 = Employee("asif", "khan", 50000)
dev_1 = Developer("asif", "khan", 50000, "python")
dev_2= Developer("asad", "zaman", 60000, "java")

man_1 = Manager("sami", "khan", 90000, [dev_1])
print(isinstance(Manager, Developer))


# print(man_1.email)
# man_1.add_emp(dev_2)
# man_1.remove_emp(dev_1)
# man_1.print_emps()


# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
# print(dev_1.prog_lang)
# print(dev_2.email)

# print(help(Developer))
   
# print(dev_1.email)
# print(dev_2.email)
    
# import datetime
# my_date = datetime.date(2024, 6, 18)    

# print(Employee.is_workday(my_date))


# emp_str1 = "jgon-khan-50000"
# emp_str2 = "poas-zaman-60000"   
# emp_str3 = "kokah-khan-70000"

# first, last, pay = emp_str1.split("-")
# new_emp1 = Employee.from_string(emp_str1)

# dev_1.set_raise_amount(1.04)

# print(new_emp1.email)
# print(new_emp1.pay)

# print(emp1.email)
# print(emp2.email)

# print(emp1.fullname())
# print(emp2.fullname())
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)


# print('{} {}'.format(emp1.fisrt, emp1.last)) 


# def outer():
#     def inner():
#         print("this is inner function")
#     print("this is outer function")
#     return inner 


# print(outer()())
# # outer()()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(" parent class method called")


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name,salary)
        self.language = language
        super().display()

        


dev = Developer("Asif", 30000, "Python")

print(dev.name)
print(dev.salary)
print(dev.language)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"
        
    def __add__(self,other):
         return self.salary + other.salary

    def __len__(self):
        return len(self.name)


emp_1 = Employee("Asif", 30000)
emp_2 = Employee("Zaman", 40000)


print(emp_1)

print(len(emp_2))  

print(emp_1 + emp_2)  # Output: 70000


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return "Person('{}', '{}')".format(self.name, self.age)

  def __repr__(self):
    return "Person('{} - '{}')".format(self.name, self.age)

p1 = Person("Emil", 36)
p2 = Person("Tobias", 30)

# print(p1)
print(repr(p1))
print(str(p1))  # str is used to create output for end users, while repr is used for debugging and development.
# repr(p1)  # repr mostly used for debugging and development, while str is used for creating output for end users.




print(emp_1 + emp_2)  # Output: 70000