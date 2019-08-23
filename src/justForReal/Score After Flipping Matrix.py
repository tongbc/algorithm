class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        a,b = len(A),len(A[0])
        res = 0
        lis = [0]*b
        for i in range(a):
            if A[i][0]==0:
                for j in range(1,b):
                    if A[i][j]==0:
                        lis[j]+=1
            else:
                for j in range(1,b):
                    if A[i][j]==1:
                        lis[j]+=1
        res+=a*(2**(b-1))
        for i in range(1,len(lis)):
            res+=max(lis[i],a-lis[i])*(2**(b-1-i))
        return res