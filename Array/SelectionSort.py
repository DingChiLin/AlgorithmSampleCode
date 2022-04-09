def selection_sort(arr):
	for i in range(len(arr)):
		min_value = arr[i]
		min_index = i
		for j in range(i, len(arr)):
			if arr[j] < min_value:
				min_value = arr[j]
				min_index = j
		arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [1,4,7,3,2,9,6,8,5]
selection_sort(arr)
print(arr)
