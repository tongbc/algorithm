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