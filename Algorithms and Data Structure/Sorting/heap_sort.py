from test_sorting import test
def heapify(arr,i,n):
    largest = i
    left_child = 2*i+1
    right_child = 2*i+2
    if left_child < n and arr[largest] < arr[left_child]:
        largest = left_child
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child
    if i != largest:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,largest,n) 

def build_heap(arr,start,end):
    for i in range(end//2 -1,start-1,-1):
        heapify(arr,i,end)

def delete_max(arr,start,end):
    arr[start],arr[end-1] = arr[end-1],arr[start]
    heapify(arr,start,end-1)

def heap_sort(arr,start,end):
    n = end + 1
    build_heap(arr,start,n)

    for i in range(n-1):
        delete_max(arr,start,n-i)

# l = [3, 6, 7, 8, 11, 16, 16, 19, 22, 26, 35, 35, 36, 37, 39, 40, 43, 43, 46, 49, 53, 55, 56, 57, 58, 58, 59, 60, 61, 62, 62, 66, 69, 70, 74, 75, 76, 79, 81, 87, 91, 91, 96, 100, 75]
# heap_sort(l,0,len(l))
# print(l) 

if __name__ == "__main__":
    test(heap_sort)
    # pass