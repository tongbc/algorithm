class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        low,high = 0,len(A)-1
        while(low<=high):
            mid = (low+high)//2
            if(A[mid]>A[mid-1] and A[mid]>A[mid+1]):
                return mid
            elif(A[mid]>A[mid-1]):
                low=mid+1
            elif(A[mid]>A[mid+1]):
                high = mid-1
        return low