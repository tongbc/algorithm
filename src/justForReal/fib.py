class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==1:
            return 1
        elif N==0:
            return 0
        return self.fib(N-1)+self.fib(N-2)

    def fib(self,N):
        a,b = 0,1
        for _ in range(N):
            a,b = b,a+b
        return a