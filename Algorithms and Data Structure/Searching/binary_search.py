def binary_search(arr,start,end,target):
    if start > end:
        return -1
    mid = (start + end) //2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(arr,start,mid-1,target)
    return binary_search(arr,mid+1,end,target)

def binary_serach_iter(arr,target):
    start,end = 0,len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return -1

l = [1,2,3,4,5]
# print(binary_search(l,0,len(l)-1,1))
# print(binary_search(l,0,len(l)-1,3))
# print(binary_search(l,0,len(l)-1,10))
# print(binary_search(l,0,len(l)-1,0))
# print(binary_search(l,0,len(l)-1,6))

print(binary_serach_iter(l,1))
print(binary_serach_iter(l,3))
print(binary_serach_iter(l,6))
print(binary_serach_iter(l,0))
print(binary_serach_iter(l,5))