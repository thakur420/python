def compare(a,b):
    if len(a) != len(b):
        return len(a) < len(b)
    if a > b :
        return False
    return True

def merge(arr,start,mid,end):
    left_list = arr[start:mid+1]
    right_list = arr[mid+1:end+1]
    m,n = len(left_list),len(right_list)
    i,j,k = 0,0,0
    while i < m and j < n:
        if compare(left_list[i],right_list[j]):
            arr[start+k] = left_list[i]
            i += 1
        else:
            arr[start+k] = right_list[j]
            j += 1
        k += 1 
    while i < m:
        arr[start+k] = left_list[i]
        i += 1
        k += 1
    while j < n:
        arr[start+k] = right_list[j]
        j += 1
        k += 1

def merge_sort(arr,start,end):
    if start >= end:
        return
    mid = (start + end)//2
    merge_sort(arr,start,mid)
    merge_sort(arr,mid+1,end)
    merge(arr,start,mid,end)


l = ["emli","jackfruit","apple","date","banana", "cherry"]
merge_sort(l,0,len(l)-1)
print(l)