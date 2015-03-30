
def insert_sort(arr):
    n = len(arr)
    for j in range(1, n):
        a = arr[j]
        i = j
        while i>0 and arr[i-1] > a:
            arr[i] = arr[i-1]
            i = i - 1
        arr[i] = a


arr = [5,2,3,1]

insert_sort(arr)

print arr
