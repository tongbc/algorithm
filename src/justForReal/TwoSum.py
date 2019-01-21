class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<2:
            return 
        dic = {}
        for index,i in enumerate(nums):
            if i in dic:
                return [dic[i],index]
            else:
                dic[target-i]=index