print ("Hello World");
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
c= a+b
print("So the sum of {} and {} is {}".format(a,b,c))
name = "John"
age = 25
print(name, age)
print("My name is {} and I am {} years old".format(name, age))
x = 10          # int
y = 3.14        # float
name = "Alice"  # string
is_active = True  # bool

print(type(x))
print(type(y))  
print(type(name))
print(type(is_active))

a = input("Enter a number: ")
print("You entered:", a)

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
elif age > 12:
    print("You are a teenager.")
else:
    print("You are a child.")



for i in range(age):
    print(i)


x = 0
while x < 5:
    print(x)
    x += 1


def hello(world):
    print("hello", world);

hello("world")

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  
fruits.append("orange")
print(fruits)
fruits.pop(1)
print(fruits)
fruits.remove("apple")
print(fruits)