import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m = (int)(math.pow(3,(int)(math.log(0x7fffffff)/math.log(3))))
        return ( n>0 and  m%n==0)
