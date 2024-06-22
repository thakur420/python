import random
import time

def result_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def test(fun):
    n = random.randint(1,100)
    print(f"testing for {n} random array of input")
    for i in range(n):
        m = random.randint(10,100)
        arr_copy = arr = [random.randint(1,100) for _ in range(m)]
        fun(arr,0,len(arr)-1)
        if not result_sorted(arr):
            print(arr_copy)
            print(arr)
            break
    print("All test case passed")

if __name__ == "__main__":
    pass