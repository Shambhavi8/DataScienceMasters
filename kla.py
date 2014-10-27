# This is a linear algebra package that I wrote to solve
# my dual need to master linear algebra as well as improve
# my python skills which are (admittedly) quite rusty at
# the moment.
# 
# 2014

import math

myMatrix = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16],
	[17,18,19,29],]

I = [
	[1,0,0,0],
	[0,1,0,0],
	[0,0,1,0],
	[0,0,0,1],]

def strassenmultiply(a,b):
	if(len(a)==len(b) and isSquare(a)):
		return "ok"

def isSquare(a):
	if len(a[0])==len(a):
		return True
	return False

def is2n(a):
	if len(a) >= len(a[0]):
		if math.log(len(a), 2).is_integer():
			return 0, 'c'
		else:
			return (2**(int(math.log(len(a),2))+1))-len(a), 'c'
	else:
		if math.log(len(a[0]), 2).is_integer():
			return 0, 'r'
		else:
			return 2**(int(math.log(len(a[0]),2))+1)-len(a[0]), 'c'

def squareUp(a, n, which='r'):
	if which == 'c':
		for i in range(n):
			for j in a:
				j.append(0)

	if which == 'r':
		r=[]
		for i in range(len(a[0])):
			r.append(0)
		for j in range(n):
			a.append(r)

n, which = is2n(myMatrix)
print myMatrix
squareUp(myMatrix,n,which)
print myMatrix