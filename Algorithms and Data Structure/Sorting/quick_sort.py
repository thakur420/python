
import time
from test_sorting import test

def partition(arr,start,end):
    PIVOT_IDX = start
    pivot_ele = arr[PIVOT_IDX]
    while start < end :
        while start < end and arr[start] <= pivot_ele:
            start += 1
        while arr[end] > pivot_ele:
            end -= 1
        if start < end:
            arr[start],arr[end] = arr[end],arr[start]
    arr[PIVOT_IDX],arr[end] = arr[end],arr[PIVOT_IDX]
    return end

def quick_sort(arr,start,end):
    if start >= end :
        return
    partition_idx = partition(arr,start,end)
    quick_sort(arr,start,partition_idx-1)
    quick_sort(arr,partition_idx+1,end)

if __name__ == "__main__":
    test(quick_sort)