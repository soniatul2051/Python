nums = [4, 7, 2, 7, 9, 2, 4, 7]
seen =[]
duplicates = []

for i in nums:
    if i in seen:
       if i not in  duplicates:
           duplicates.append(i)
    else:
        seen.append(i)

print(duplicates)
print(seen)
        
      
