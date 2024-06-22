def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

l = [1, 3, 5, 7, 9, 11]
print(linear_search(l,5))
print(linear_search(l,6))