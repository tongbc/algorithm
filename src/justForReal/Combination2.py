class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.dfs(candidates,0,[],[],target)
    def dfs(self, candidates,start,res,ans,target):
        if target<0:
            return
        if target==0:
            res.append(ans)
            return
        for i in range(start,len(candidates)):
            if i!=start and candidates[i]==candidates[i-1]:
                continue
            self.dfs(candidates,i+1,res,ans+[candidates[i]],target-candidates[i])
        return res


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        cand = sorted(candidates)
        self.part(0, [], cand, target, res)
        return res

    def part(self, i, p, nums, target, res):
        if target == 0:
            res.append(p)
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue
            if nums[j] > target:
                break
            self.part(j + 1, p + [nums[j]], nums, target - nums[j], res)

