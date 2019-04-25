class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [[1]*(i+1) for i in range(rowIndex+1)]
        for i in range(1,rowIndex+1):
            for j in range(1,i):
                res[i][j] = res[i-1][j-1]+res[i-1][j]
        return res[rowIndex]

sol = Solution()
print(sol.getRow((3)))