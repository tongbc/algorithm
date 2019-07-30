class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res,m = 0,0
        for i in range(len(arr)):
            m = max(m,arr[i])
            if m==i:
                res+=1
        return res