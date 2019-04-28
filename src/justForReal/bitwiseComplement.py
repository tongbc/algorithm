class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        X = 1
        while N > X: X = X * 2 + 1
        return X - N