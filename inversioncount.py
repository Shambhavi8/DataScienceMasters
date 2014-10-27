# This script uses a merge sort algorithm to count the
# number of inversions in an array of integers

# fname = "IntegerArray.txt"
# with open(fname) as f:
#	myList = f.readlines()

# myList = []

f = open("IntegerArray.txt")
myList = list()
for line in f:
	myList.append(int(line))


def count_inv(a):
	return count(a)[1]

def count(a):
	if len(a) <= 1: return a, 0;
	mid = len(a)/2
	left, x = count(a[:mid])
	right, y = count(a[mid:])
	result, z = count_split_inv(left, right)
	return result, x + y + z

def count_split_inv(left, right):
	result = []
	count = 0
	i, j = 0, 0;
	left_len = len(left)
	while(i < left_len and j < len(right)):
		if left[i]<= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			count += left_len - i
			j+= 1
	result += left[i:]
	result += right[j:]
	return result, count

print count(myList)[1]