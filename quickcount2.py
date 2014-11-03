count = 0
#import sys
#sys.setrecursionlimit(10010000)

f = open("Quicksort.txt")
a = list()
for line in f:
	a.append(int(line))

def bigger(a,b):
    if a > b:
        return a
    else:
        return b
        
def biggest(a,b,c):
    return bigger(a,bigger(b,c))
  
def median(a,b,c):
    largest = biggest(a,b,c)
    if a == largest:
        median = bigger(b, c)
    elif b == largest:
        median = bigger(a, c)
    else:
        median = bigger(a, b)
    return median

def partition(a,l,r):
	
	global count 
	count = count + len(a[l:r])
	#print count
	#print l
	#a[l], a[r] = a[r], a[l] #--------------------> for part 2 of the question
	
	e = median(a[l], a[(l+r)/2], a[r])
	x = a.index(e)              #----------------------> for part 3 of question
	a[l], a[x] = a[x], a[l]
	
	p = a[l]
	i = l + 1
	j = 0
	j = l + 1
	while j <=r:
		if a[j] < p:
			
			a[i], a[j] = a[j], a[i]
			i = i + 1
		j = j + 1
	a[l], a[i-1] = a[i-1], a[l]
	#print a
	return (i-1)
	
def quicksort(a,l,r):
	if l < r:
		j = partition(a,l,r)
		quicksort(a,l,j-1)
		#if (j-1) >= 0:
		quicksort(a,j+1,r)
	return a

print quicksort(a,0,a.index(a[-1]))
print count