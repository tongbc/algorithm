##dumb DFS
import copy
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        lis = [i for i in range(1, 10)]
        res = []
        self.dfs(k, lis, n, [], res)
        return res

    def dfs(self, num, k, target, sour, res):
        # if target == 0 and num==0 :
        #     res.append(sour)
        #     return
        if num == 1 and target > 9 - len(k) and target < 10:
            sour.append(target)
            res.append(sour)
            return
        if target < 0 or len(k) == 0 or num > len(k):
            return
        if num == 0:
            return
        temp = copy.deepcopy(k)
        temp.remove(temp[0])
        self.dfs(num - 1, temp, target - k[0], sour + [k[0]], res)
        self.dfs(num, temp, target, sour, res)


## back tracking
class Solution:
    def combinationSum3(self, k, n):

        def generate(start, item, result, nums, n):
            if n < 0 or len(item) > k:
                return
            if len(item) == k - 1 and (n > low or n < low - len(nums)):
                return
            if n == 0:
                if len(item) == k:
                    result.append(list(item))
                    return
            for j in range(start, len(nums)):
                item.append(nums[j])
                generate(j + 1, item, result, nums, n - nums[j])
                item.pop()

        low = min(10, n)
        nums = range(1, low)
        item = []
        result = []
        generate(0, item, result, nums, n)
        return result