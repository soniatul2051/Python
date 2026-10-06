nums = [8, 3, 12, 5, 1, 9, 6]

small = nums[0]

for i in nums:
   if small > i:
       small = i

print(small)
