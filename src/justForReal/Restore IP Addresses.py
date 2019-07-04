class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                continue
            else:
                for j in range(l-1, i,-1 ):
                    if nums[j] > nums[i]:
                        self.swap(nums, j, i)
                        self.reverse(nums,i+1,l-1)
                        ## 改进：不需要排序，因为插入的位置
                        # nums[i + 1:] = sorted(nums[i + 1:])
                        return nums
        self.reverse(nums,0,l-1)
        return nums

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp

    def reverse(self,nums,l,r):
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1