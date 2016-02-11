from collections import Counter

def findp4(p1,p2,p3):
	xlis = list()
	ylis = list()
	xlis.append(int(p1.split(' ')[0]))
	xlis.append(int(p2.split(' ')[0]))
	xlis.append(int(p3.split(' ')[0]))

	ylis.append(int(p1.split(' ')[1]))
	ylis.append(int(p2.split(' ')[1]))
	ylis.append(int(p3.split(' ')[1]))

	cntx = Counter(xlis)
	cnty = Counter(ylis)

	p4_x = cntx.most_common()[-1]
	p4_y = cnty.most_common()[-1]

	return str(p4_x[0]) + ' ' + str(p4_y[0])


	c.most_common()[:-n-1:-1]

for i in range(input()):
	p1=raw_input()
	p2=raw_input()
	p3=raw_input()
	p4=findp4(p1,p2,p3)
	print p4
	