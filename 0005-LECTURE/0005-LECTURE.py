for i in range(input()):
	s=raw_input()
	rep=len(s)/2
	st = [None]*rep
	for i in range(rep):
		st[i]=s[i*2:i*2+2]
	newst = sorted(st)
	print ''.join(newst)