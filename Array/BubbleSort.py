def bubble_sort(arr):
	for i in range(len(arr)-1, -1, -1):
		for j in range(i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [1,4,7,3,2,9,6,8,5]
bubble_sort(arr)
print(arr)
