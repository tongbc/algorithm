class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        a = [0] * col
        b = [0] * row
        count = 0
        for j in range(col):
            m = -0xfffffff
            for i in range(row):
                m = max(m, grid[i][j])
            a[j] = m
        for i in range(row):
            m = -0xfffffff
            for j in range(col):
                m = max(m, grid[i][j])
            b[i] = m
        for i in range(row):
            for j in range(col):
                temp = min(b[i], a[j])
                count = count + (temp - grid[i][j])
        return count

###
    def maxIncreaseKeepingSkyline(self, grid):
        row, col = map(max, grid), map(max, zip(*grid))
        return sum(min(i, j) for i in row for j in col) - sum(map(sum, grid))