def add(x,y,a):
    a = x+y
    return a

def sub(x,y,a):
    a = x-y
    return a

def mult(x,y,a):
    a = x*y
    return a

def divide(x,y,a):
    a = x/y
    return a

print("Welcome to Bella's Basic Calculator")
x = float(input("Enter the first number: "))
valid_ops = ["+", "-", "*", "/"]
op = input("Enter an operator (+,-,*,/): ")
y = float(input("Enter the second number: "))

