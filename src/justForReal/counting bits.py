class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0]
        for i in range(1, num + 1):
            half = i / 2
            if i % 2 == 0:
                dp.extend([dp[int(half)]])
            else:
                dp.extend([dp[int(half)] + 1])
        return dp
