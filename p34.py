def analyze_numbers(numbers):
    even = []
    odd =[]
    even_sum = 0
    odd_sum = 0
    for i in numbers:
       if i % 2 == 0:
          even.append(i)
       else:
          odd.append(i)

    for i in even:
       even_sum = even_sum + i
    for i in odd:
       odd_sum = odd_sum + i
    return {
            "even": even,
            "odd": odd, 
            "even_sum": even_sum,
            "odd_sum": odd_sum
     }




numbers = [4, 7, 12, 5, 18, 7, 20, 3, 10]

result = analyze_numbers(numbers)

print(result)
