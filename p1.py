a = [1, 2, 3]
b = a

b.append(4)
b = b + [5]

print(a)
print(b)
print(a is b)
