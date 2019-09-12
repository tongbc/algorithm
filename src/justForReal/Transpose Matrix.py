class Solution:
    def transpose(self, lis):
    # def transpose(self, lis):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        a,b = len(lis),len(lis[0])
        res = [[0]*a for i in range(b)]
        for i in range(a):
            for j in range(b):
                res[j][i] = lis[i][j]
        return res

print(bin(2))