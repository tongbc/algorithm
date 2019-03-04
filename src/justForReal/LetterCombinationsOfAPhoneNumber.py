class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        lis = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"],
               ["p", "q", "r", 's'], ["t", "u", "v"], ["w", "x", "y", "z"]]
        res = []
        part = ""
        self.dfs(digits, lis, part, res)
        return res

    def dfs(self, nums, lis, part, res):
        if not nums:
            res.append(part)
        else:
            num = int(nums[0]) - 2
            for let in lis[num]:
                self.dfs(nums[1:], lis, part + let, res)