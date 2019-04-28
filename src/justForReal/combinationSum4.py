class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        self.dfs(0,nums,[],target,res)
        return res

    def dfs(self,start,nums,lis,target,res):
        if target == 0:
            res.append(lis)
            return
        if target<nums[start]:
            return
        for index,i in enumerate(nums[start:]):
            self.dfs(start+index,nums,lis+[i],target-i,res)

sol = Solution()
# nums = [1,2,3]
# target = 4
# print(sol.combinationSum4(nums,target))
print([1]+[0]*5)