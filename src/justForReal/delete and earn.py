class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0)+num
        res = [0]
        key_set = set()
        for k,v in sorted(dic.items()):
            if k-1 not in key_set:
                key_set.add(k)
                res.append(res[-1]+v)
            else:
                key_set.add(k)
                res.append(max(res[-2]+v,res[-1]))
        return res[-1]