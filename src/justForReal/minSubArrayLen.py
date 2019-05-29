class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = []
        mark = ()
        if not nums:
            return 0
        if nums[0]>=s:
            return 1
        else:
            mark=(1,nums[0])
        for i in range(1,len(nums)):
            if nums[i]+mark[1]>=s:
                temp = nums[i]+mark[1]
                count = 0
                while(temp>=s):
                    temp-=nums[i-mark[0]+count]
                    count+=1
                res.append(mark[0]+2-count)
                mark=((1+mark[0]-count,temp))
            else:
                mark=((1+mark[0],nums[i]+mark[1]))
        if not res:
            return 0
        return min(res)