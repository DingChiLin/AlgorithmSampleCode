def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while key < arr[j] and j >= 0:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key

arr = [1,4,7,3,2,9,6,8,5]
insertion_sort(arr)
print(arr)
