def rotate(self, matrix):
	"""
	:type matrix: List[List[int]]
	:rtype: void Do not return anything, modify matrix in-place instead.
	"""
	matrix.reverse()
	for i in range(len(matrix)):
		for j in range(i):
			temp = matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = temp


A = [1,2,3,4,5,6]
print(A[:3],A[4:])