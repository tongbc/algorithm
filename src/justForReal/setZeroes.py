class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.mark0(matrix, i, j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1000:
                    matrix[i][j] = 0

    def mark0(self, matrix, a, b):
        for i in range(len(matrix)):
            if (i == a) or (matrix[i][b] == 0):
                continue
            matrix[i][b] = 1000
        for j in range(len(matrix[0])):
            if (b == j) or (matrix[a][j] == 0):
                continue
            matrix[a][j] = 1000

