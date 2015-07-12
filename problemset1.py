# Count inversions in array
# Base n=1, inversions 0
# Else count left, count right
splits = 0

def merge_sort(arr):
	global splits
	if len(arr) > 1:
		mid = len(arr) // 2
		left = arr[:mid]
		right = arr[mid:]

		merge_sort(left)
		merge_sort(right)

		i,j,k = 0,0,0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
				splits += len(left[i:])
			k += 1
			
		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1

def main():
	global splits
	f_handler = open("IntegerArray.txt")
	arr = [int(x) for x in f_handler]
	merge_sort(arr)
	print splits

main()