#xor solution

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        res = []
        for num in nums:
            try:
                dic[num] = dic[num] + 1
            except:
                dic[num] = 1
        for key in dic:
            if dic[key] == 1:
                res.append(key)
        return res
