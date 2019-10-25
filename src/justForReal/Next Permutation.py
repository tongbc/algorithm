# class Solution(object):
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         l = len(nums)
#         for i in range(l - 2, -1, -1):
#             if nums[i] >= nums[i + 1]:
#                 continue
#             else:
#                 for j in range(l-1, i,-1 ):
#                     if nums[j] > nums[i]:
#                         self.swap(nums, j, i)
#                         nums[i + 1:] = sorted(nums[i + 1:])
#                         return nums
#         self.reverse(nums,0,l-1)
#         return nums
#
#     def swap(self, nums, a, b):
#         temp = nums[a]
#         nums[a] = nums[b]
#         nums[b] = temp
#
#     def reverse(self,nums,l,r):
#         while l < r:
#             nums[l],nums[r] = nums[r],nums[l]
#             l += 1
#             r -= 1


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = len(nums) - 1, len(nums) - 1
        while (i > 0 and nums[i] <= nums[i - 1]):
            i -= 1
        if i == 0:
            self.re(nums, 0, j)
            return
        while (nums[j] <= nums[i - 1]):
            j -= 1
        temp = nums[i - 1]
        nums[i - 1] = nums[j]
        nums[j] = temp
        self.re(nums, i, len(nums) - 1)

    def re(self, nums, i, j):
        while (i < j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1