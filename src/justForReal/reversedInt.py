class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        sigh = +1 if x>0 else -1
        x = x if x>0 else -x
        while x!=0:
            res = res*10 +x%10
            x = x//10
        return sigh*(res  if -(2**31)-1 < res < 2**31 else 0)