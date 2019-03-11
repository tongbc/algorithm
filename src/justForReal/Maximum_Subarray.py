class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = self.part(nums)
        return res
    def part(self,nums):
        if len(nums)==1:
            return nums[0]
        else:
            half = len(nums)//2
            a,b = nums[:len(nums)//2],nums[len(nums)//2:]
            res1,res2 = self.part(a),self.part(b)
            lmax = nums[half-1]
            su =nums[half-1]
            for i in range(half-2,-1,-1):
                su+=nums[i]
                lmax = max(lmax,su)
            rmax = nums[half]
            su =nums[half]
            for i in range(half+1,len(nums)):
                su+=nums[i]
                rmax = max(rmax,su)
            return max(res1,res2,rmax+lmax)

sol = Solution()
print(sol.maxSubArray([1,1]))
