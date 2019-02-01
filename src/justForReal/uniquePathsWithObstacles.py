def uniquePathsWithObstacles(obstacleGrid):
	"""
	:type obstacleGrid: List[List[int]]
	:rtype: int
	"""
	if obstacleGrid[0][0]:
		return 0
	n,m = len(obstacleGrid),len(obstacleGrid[0])
	dp = [([0] * m) for _ in range(n)]
	# for i in range(n):
	# 	dp[i][0] = 1
	flag = True
	for i in range(m):
		if not flag:
			dp[0][i] = 0
		if obstacleGrid[0][i] ==1:
			dp[0][i] = 0
			flag = False
			continue
		dp[0][i] = 1
	flag = True
	for i in range(n):
		if not flag:
			dp[i][0] = 0
		if obstacleGrid[0][i] ==1:
			dp[i][0] = 0
			flag = False
			continue
		dp[i][0] = 1
	for row in range(1, n):
		for col in range(1, m):
			if obstacleGrid[row][col] ==1:
				dp[row][col] = 0
			else:
				dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
	return dp[n - 1][m - 1]


def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, r):
            dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])
        for i in range(1, c):
            dp[0][i] = dp[0][i-1] * (1 - obstacleGrid[0][i])
        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1 - obstacleGrid[i][j])
        return dp[-1][-1]