__author__ = 'Sundong Kim'
import sys
lines = sys.stdin.readlines()
num_building = int(lines[0])
for i in range(1, num_building+1):
    j = 2*i
    vals = lines[j].replace('\n','')
    result = vals.split(' ')
    sums = map(int, result)
    if(int(lines[j-1]) >= sum(sums)):
        print 'YES'
    else:
        print 'NO'