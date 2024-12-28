import array 

arr = array.array("i", [1, 2, 3, 4, 5])
print(arr)


arr.insert(2, 10)
print(arr)

arr.remove(10)
print(arr)

arr.pop(2)
print(arr)

for i in range(len(arr)):
    print(arr[i])

print(arr)
