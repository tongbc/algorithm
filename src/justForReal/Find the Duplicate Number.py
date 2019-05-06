class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return -1
        low,high = 0,len(nums)-1
        mid = (low+high)/2
        while(high-low>1):
            count = 0
            for k in nums:
                if mid<k<=high:
                    count+=1
            if count >high-mid:
                low = mid
            else:
                high = mid
            mid = (low+high)/2
        return high