class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <3:
            return 0
        prim = [True]*n
        prim[0],prim[1] = False,False
        for i in range(2,int(n**0.5)+1):
            if prim[i]:
                prim[i*i:n:i] = [False]*len(prim[i*i:n:i])
        return sum(prim)