import math
import math


class Solution(object):
    # def topKFrequent(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #     res = [(0, 0) for i in range(k)]
    #     map = {}
    #     for i in range(nums):
    #         if i not in map.keys():
    #             map[i] = 1
    #         else:
    #             map[i] += 1
    #     for key in map:

    def left(self, num):
        return num * 2 + 1

    def right(self, num):
        return num * 2 + 2

    def max_heapify(self, nums, i):
        l, r = self.left(i), self.right(i)
        if l < len(nums) and nums[i] < nums[l]:
            largest = l
        else:
            largest = i
        if r < len(nums) and nums[largest] < nums[r]:
            largest = r
        if (largest != i):
            self.swap(nums, largest, i)
            self.max_heapify(nums,largest)

    def build_max_heap(self,nums):
        for i in range(math.floor((len(nums) - 1) / 2), -1, -1):
            self.max_heapify(nums, i)

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def pop_max(self,nums):
        max = (nums[0])
        nums[0] = nums[-1]
        nums = nums[:-1]
        self.max_heapify(nums,0)
        return max,nums
sol = Solution()
nums = [1,2,3,4,5,6,7,8]
sol.build_max_heap(nums)
print(nums)
max, nums = sol.pop_max(nums)
print(nums)