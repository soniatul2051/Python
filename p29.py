numbers = [12, 5, 8, 21, 7, 30, 14, 9, 18]

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
       even.append(i)
    else:
       odd.append(i)

print(even)
print(odd)

even_sum = 0
for i in even:
    even_sum = even_sum + i

odd_sum = 0
for i in odd:
    odd_sum = odd_sum + i

print(even_sum)
print(odd_sum)
