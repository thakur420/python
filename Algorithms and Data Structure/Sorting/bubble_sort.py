import timeit
import random
from test_sorting import test

def bubble_sort(arr,start,end):
    n = len(arr)
    for i in range(n-1):
        is_swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                is_swapped = True
        if not is_swapped:
            break

# l = [5,4,3,2,1]
# print(l)
# bubble_sort(l)
# print(l)

# random_list = [random.randint(0,10000) for _ in range(10000)]
# bubble_sort_time = timeit.timeit(lambda: bubble_sort(random_list), number=1)
# print(f'Bubble sort time: {bubble_sort_time:.6f} seconds')

if __name__ == "__main__":
    test(bubble_sort)