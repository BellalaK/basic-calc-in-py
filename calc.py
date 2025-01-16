def add(x,y):
    a = x+y
    return a

def sub(x,y):
    a = x-y
    return a

def mult(x,y):
    a = x*y
    return a

def divide(x,y):
    a = x/y
    return a

print("Welcome to Bella's Basic Calculator")
valid_ops = ["+", "-", "*", "/"]

x = float(input("Enter the first number: "))

while True:
    op = input("Enter an operator (+,-,*,/): ")
    if op in valid_ops:
        break
    
y = float(input("Enter the second number: "))

if op == valid_ops[0]:
    add(x,y)
elif op == valid_ops[1]:
    sub(x,y)
elif op == valid_ops[2]:
    mult(x,y)
elif op == valid_ops[3]:
    divide(x,y)
    