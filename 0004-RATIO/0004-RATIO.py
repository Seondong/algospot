from __future__ import division
import math

def findX(N,M,Z):
	X = math.ceil((N*Z+N-100*M)/(99-Z))
	if X <= 0:
		return -1
	else:
		return int(X)

for i in range(input()):
	s=raw_input().split(' ')
	N=float(s[0])
	M=float(s[1])
	Z = int(M/N * 100)
	print findX(N,M,Z)