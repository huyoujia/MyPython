'''
def print_menu():
	sum = 0
	ossum = 0
	jssum = 0
	for i in range(0,101):
		if i%2==0:
			ossum += i
		else:
			jssum += i
		sum +=i
	print("偶数和%s"%ossum)
	print("奇数和:%s"%jssum)
	print("0到100间的和是%s"%sum)
print_menu()
'''

def print_menu():
	for i in range(1,10):
		for j in range(1,i+1):
			print("%d*%d=%d"%(j,i,j*i),end="\t")
		print("")
print_menu()
