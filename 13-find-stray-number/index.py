def stray(arr):
    if arr[0] == arr[1]:
        etalon = arr[0]
    else:
        etalon = arr[2]
    
    for num in arr:
        if num != etalon:
            return num

print(stray([1, 1, 1, 1, 1, 1, 2]))
print(stray([2, 3, 2, 2, 2]))
print(stray([3, 2, 2, 2, 2]))
