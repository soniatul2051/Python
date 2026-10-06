a = [10, 20]
b = a

a.append(30)

c = a

c.append(40)

print(a)
print(b)
print(c)
print(a is b)
print(a is c)
