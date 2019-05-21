class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = set([])
        while(n not in a):
            a.add(n)
            num = 0
            while(n>0):
                remain = n%10
                num += remain**2
                n = n/10
            if num==1:
                return True
            else:
                n = num
        return False