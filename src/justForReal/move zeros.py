class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag = True
        f = 0
        for i in range(len(nums)):
            if flag:
                if nums[i] != 0:
                    continue
                else:
                    flag = False
                    f = i
            else:
                if nums[i] == 0:
                    continue
                else:
                    self.swap(nums, i, f)
                    f = f + 1

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp