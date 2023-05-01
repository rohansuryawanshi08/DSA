def kth_smallest(arr, k):
    arr.sort()
    return arr[k-1]

def kth_largest(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]
