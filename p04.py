def sum(a,b):
    return a+b;

def sub(a,b):
    return a-b;

def mul(a,b):
    return a*b;

def div(a,b):
    return a/b;

def mod(a,b):
    return a%b;

def power(a,b):
    return a**b

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print("The sum of", a, "and", b, "is", sum(a,b))
print("The difference of", a, "and", b, "is", sub(a,b))
print("The product of", a, "and", b, "is", mul(a,b))
print("The quotient of", a, "and", b, "is", div(a,b))
print("The remainder of", a, "and", b, "is", mod(a,b))
print("The power of", a, "and", b, "is", power(a,b))
