numbers = [2, 7, 11, 15]
target = 9

for i in numbers:
    for j in numbers:
        value = i + j
        if target == value:
             print(j)
             print(i)
