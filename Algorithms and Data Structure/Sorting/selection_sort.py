import random
import timeit
from test_sorting import test

def find_max_idx(arr):
    max_val,max_idx = 0,0
    for i,x in enumerate(arr) :
        if x > max_val :
            max_val, max_idx = x,i
    return max_idx

def selection_sort(arr,start,end):
    n = len(arr)
    for i in range(n):
        # print(arr)
        max_idx = find_max_idx(arr[0:n-i])
        arr[max_idx],arr[n-i-1] = arr[n-i-1],arr[max_idx]

# l = [64, 34, 25, 12, 22, 11, 90]
# print(l)
# selection_sort(l)
# print(l)

# random_list = [random.randint(0,10000) for _ in range(10000)]
# selection_sort_time = timeit.timeit(lambda: selection_sort(random_list), number=1)
# print(f'Selection sort time: {selection_sort_time:.6f} seconds')

if __name__ == "__main__":
    test(selection_sort)

