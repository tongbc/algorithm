class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        minDis = [[0] * i for i in range(1, len(triangle) + 1)]
        minDis[0][0] = triangle[0][0]
        length = len(triangle)
        for i in range(1,length):
            for j in range(len(triangle[i])):
                if j - 1 < 0:
                    minDis[i][j] = minDis[i - 1][j]+triangle[i][j]
                elif j > i - 1:
                    minDis[i][j] = minDis[i - 1][i - 1]+triangle[i][j]
                else:
                    minDis[i][j] = min(minDis[i - 1][j - 1]+triangle[i][j], minDis[i - 1][j]+triangle[i][j])
        # result = 100000
        # for i in range(length):
        #     result = min(result, minDis[length - 1][i])
        # return result
        return min(minDis[-1])
