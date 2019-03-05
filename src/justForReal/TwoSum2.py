#beats 100% solution
class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

#dic version
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        res = []
        for index, num in enumerate(numbers):
            if (target - num) in dic.keys():
                res = [dic[target - num], index + 1]
            else:
                dic[num] = index + 1
        return res
