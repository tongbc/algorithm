class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res= []
        p = 1
        length = len(nums)
        for i in range(length):
            res.append(p)
            p = p*nums[i]
        p=1
        for i in range(length-1,-1,-1):
            res[i] = res[i]*p
            p = p*nums[i]
        return res