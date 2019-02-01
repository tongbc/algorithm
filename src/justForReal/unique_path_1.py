def uniquePaths(m, n):
	"""
	:type m: int
	:type n: int
	:rtype: int
	"""
	dp = [([0]*m) for _ in range(n)]
	for i in range(n):
		dp[i][0] = 1
	for i in range(m):
		dp[0][i] = 1
	for row in range(1,n):
		for col in range(1,m):
			dp[row][col] = dp[row-1][col] + dp[row][col-1]
	return dp[n-1][m-1]

print(uniquePaths(7, 3))