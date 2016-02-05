for i in range(input()):
	s=raw_input().split(" ")
	c=int(s[0])
	s=s[1]
	print str(i+1), s[:c-1]+s[c:]