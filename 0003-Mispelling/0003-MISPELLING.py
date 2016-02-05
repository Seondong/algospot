__author__ = 'Sundong Kim'
import sys

def mispell(text):
    a = text.split(" ")
    num = int(a[0])-1
    word = a[1]
    return word[:num]+word[num+1:]

lines = sys.stdin.readlines()
num_case = int(lines[0])
for i in range(1, num_case+1):
    print str(i) + ' ' + mispell(lines[i].replace('\n',''))
