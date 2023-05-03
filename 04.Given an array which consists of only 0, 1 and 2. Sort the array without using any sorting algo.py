def sort012(arr, arr_size):
	lo = 0
	hi = arr_size - 1
	mid = 0
	while mid <= hi: 
		
		if arr[mid] == 0:
			arr[lo], arr[mid] = arr[mid], arr[lo]
			lo = lo + 1
			mid = mid + 1
		
		elif arr[mid] == 1:
			mid = mid + 1
		
		else:
			arr[mid], arr[hi] = arr[hi], arr[mid]
			hi = hi - 1
	return arr


def printArray(arr):
	for k in arr:
		print(k, end=' ')
