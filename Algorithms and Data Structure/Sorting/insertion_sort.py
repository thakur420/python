import random
import timeit
from test_sorting import test
def insertion_sort(arr,start,end):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key 

# l = [1,2,3,4,5]
# print(l)
# insertion_sort(l)
# print(l) 

# random_list = [random.randint(0,10000) for _ in range(10000)]
# insertion_sort_time = timeit.timeit(lambda: insertion_sort(random_list), number=1)
# print(f'Insertion sort time: {insertion_sort_time:.6f} seconds')

if __name__ == "__main__":
    test(insertion_sort)