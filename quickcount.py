# This script uses quicksort to sort an array of integers
# and counts the number of comparisons needed to do so

f = open("Quicksort.txt")
myList = list()
for line in f:
	myList.append(int(line))

count  = 0

def partition(list, l, e, g):
    global count
    while list != []:
        head = list.pop(0)
        if head < e[0]:
            l = [head] + l
        elif head > e[0]:
            g = [head] + g
        else:
            e = [head] + e
    return (l, e, g)

def qsort2(list):
    """Quicksort using a partitioning function"""
    global count
    if list == []: 
        return []
    else:
        pivot = choosemed(list[0], list[len(list)/2], list[len(list)-1])
        lesser, equal, greater = partition(list[1:], [], [pivot], [])
        count += (len(lesser)-1 + len(greater)-1)
        return qsort2(lesser) + equal + qsort2(greater)

def median(mylist):
    sorts = sorted(mylist)
    length = len(sorts)
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]

def choosemed(a, b, c):
    choice = [a, b, c];
    return median(choice)

myList = qsort2(myList)

for i in range(10):
    print myList[i]

print count