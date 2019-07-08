class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return -1
        lis = ["#"]*(amount+2)
        t = []
        for num in coins:
            if num>coins:
                continue
            t.append(num)
        coins = t
        if not coins:
            return -1
        for num in coins:
            lis[num] = 1
        for i in range(1,amount+1):
            if i not in coins:
                m = 100000
                temp = []
                for num in coins:
                    if i-num<=0 or lis[i-num]=="#":
                        continue
                    else:
                        m = min (m,lis[i-num]+1)
                if m != 100000:
                    lis[i] = m
        return lis[amount] if lis[amount]!="#" else -1
sol = Solution()
print(sol.coinChange([2147483647],2))
