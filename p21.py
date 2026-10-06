nums = [4, 7, 2, 7, 9, 2, 4, 7, 10, 7]

largest = nums[0]

for i in nums:
    if  largest < i:
        largest = i

print(largest)
