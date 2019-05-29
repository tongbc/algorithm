class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = None
        c = 0
        for num in nums:
            if not major:
                major = num
                c += 1
            if major == num:
                c += 1
            elif major != num:
                c -= 1
                if c == 0:
                    major = None
        return major
