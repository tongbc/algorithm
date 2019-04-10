class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        res = 0
        m = prices[0]
        for num in prices:
            if num > m:
                res = max(res, num - m)
            else:
                m = num
        return res

