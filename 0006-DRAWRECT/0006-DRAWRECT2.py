for i in xrange(input()):
	x=y=0
	for i in xrange(3):

		p = raw_input().split()
		x = x ^ int(p[0])
		y = y ^ int(p[1])
		print int(p[0]), int(p[1])
		print x, y
	print x,y