def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        is_swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                is_swapped = True
        if not is_swapped:
            break

l = [5,4,3,2,1]
print(l)
bubble_sort(l)
print(l)