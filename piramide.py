num = 15

for i in range(1,num+1):
	for j in range(1,num-i+1):
		print(end="\t")
	for j in range(i,0,-1):
		print(j,end="\t")
	for j in range(2,i+1):
		print(j,end="\t")
	print()