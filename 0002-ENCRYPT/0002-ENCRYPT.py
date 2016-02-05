__author__ = 'Sundong Kim'
import sys

def encrypt(text):
    len(text)
    interm_result1 = text[::2]
    interm_result2 = text[1::2]
    result = interm_result1+interm_result2
    return result

lines = sys.stdin.readlines()
num_case = int(lines[0])
for i in range(1, num_case+1):
    print encrypt(lines[i].replace('\n',''))
