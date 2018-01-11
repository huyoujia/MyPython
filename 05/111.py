list = [{"beijing":{"mianji":1290,"renkou":123123,},"shanghai":{"mianji":123123,"renkou":123123}}]
for i in list:
	print(i)
	for j in i:
		print(j,i[j])
		for a in i[j]:
			print(j,a,i[j][a])
