n = 3
lis = [[0]*n]*n
# print(lis)

for i in range(n-1,-1,-1):
	top = i+1
	for j in range(i):
		lis[j][n-top] = 