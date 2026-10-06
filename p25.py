nums = [4, 7, 12, 5, 18, 7, 20, 3, 10, 7]

even_count = 0
odd_count = 0


for i in nums:
   if i % 2 == 0:
     even_count = even_count + 1
   else:
      odd_count = odd_count + 1

print("Even :", even_count)
print("Odd :", odd_count)
