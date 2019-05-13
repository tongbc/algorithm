class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix)<1 or len(matrix[0])<1:
            return False
        m,n = len(matrix[0])-1,len(matrix)-1
        col = len(matrix[0])-1
        row = 0
        while col>=0 and row<=n:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col-=1
            elif matrix[row][col]<target:
                row+=1
        return False
