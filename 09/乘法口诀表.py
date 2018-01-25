for row in range(1,10):
	col = 1
	for col in range(1,row+1):
		print("%d*%d=%d" % (col,row,row*col),end='\t')
	print("")
