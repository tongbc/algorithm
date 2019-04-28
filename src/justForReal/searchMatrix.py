#直接变成一维数组 / and % 构成行和列

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        num = len(matrix[0])
        row = len(matrix)
        low, high = 0, row - 1
        mark = 0
        flag = 0
        while (low <= high):
            mid = (low + high) // 2
            if matrix[mid][0] <= target and matrix[mid][num - 1] >= target:
                mark = mid
                flag = 1
                break
            if matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        if not flag:
            return False
        low, high = 0, num - 1
        while (low <= high):
            mid = (low + high) // 2
            if matrix[mark][mid] == target:
                return True
                break
            if matrix[mark][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
