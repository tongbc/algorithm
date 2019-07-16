class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
            return 1
        if n==3:
            return 2
        num = 1
        while(n>4):
            num*=3
            n-=3
        num*=n
        return num