class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0x7fffffff
        res = []
        for i in range(len(nums)):
            m = min(nums[i],m)
            if len(res)==0:
                res.append(m)
                continue
            if len(res)==1:
                if nums[i]>res[0]:
                    res.append(nums[i])
                else:
                    m = min(m,nums[i])
                    res[0] = m
            elif len(res)==2:
                if nums[i]>res[1]:
                    return True
                else:
                    if nums[i]>m:
                        res[0] = m
                        res[1] = nums[i]
                    else:
                        m = nums[i]
        return False

## solution 2

def increasingTriplet(nums):
    first = second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False