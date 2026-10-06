def count_even(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
           count = count + 1
    return count         

numbers = [4, 7, 12, 5, 18, 7, 20, 3, 10]

result = count_even(numbers)

print(result)
