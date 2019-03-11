import math


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        map = {}
        data = []
        for num in (nums):
            if num not in map.keys():
                map[num] = 1
            else:
                map[num] += 1
        for key in map:
            data+=[(map[key],key)]
        self.build_max_heap(data)
        print(data)
        for i in range(k):
            num,data = self.pop_max(data)
            res.append(num[1])
        return res
    def left(self, num):
        return num * 2 + 1

    def right(self, num):
        return num * 2 + 2

    def max_heapify(self, nums, i):
        l, r = self.left(i), self.right(i)
        if l < len(nums) and nums[i][0] < nums[l][0]:
            largest = l
        else:
            largest = i
        if r < len(nums) and nums[largest][0] < nums[r][0]:
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
# nums = [1,1,1,2,2,3]
# print(sol.topKFrequent(nums,2))
# sol.topKFrequent(nums,7)
# sol.build_max_heap(nums)
# print(nums)
#
# a = [(1,2),(3,4)]
# a+=[(4,5)]
# print(a)

