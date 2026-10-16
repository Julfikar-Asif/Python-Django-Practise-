def add(a,b):
    return a + b
def subtract(a,b):
    return a - b

print(__name__)  #dunder name

if __name__ == "__main__":  #dunder name and dunder main

    print("Welcome to the calculator program!")
    print("Enter two numbers: ")
    print("Enter first number: ")
    num1 = int(input())
    print("Enter second number: ")
    num2 = int(input())
    print("The sum of the two numbers is: ", add(num1,num2))
    print("The difference of the two numbers is: ", subtract(num1,num2))