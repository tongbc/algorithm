import math
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            return 0
        else:
            order = math.ceil(K / 2.0)
            num = self.kthGrammar(N - 1, math.ceil(K / 2.0))
            if num == 0:
                if K % 2 != 0:
                    return 0
                else:
                    return 1
            else:
                if K % 2 != 0:
                    return 1
                else:
                    return 0
