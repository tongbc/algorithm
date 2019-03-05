class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a, b = 0, len(nums) - 1
        rank, num = self.partition(nums, a, b)
        while (True):
            if rank + 1 == k:
                return num
            elif (rank >= k):
                b = rank - 1
                rank, num = self.partition(nums, a, rank - 1)
            else:
                a = rank + 1
                rank, num = self.partition(nums, rank + 1, b)

    def partition(self, nums, a, b):
        mark = nums[b]
        temp = a
        for i in range(a, b):
            if (nums[i] > mark):
                self.swap(nums, temp, i)
                temp += 1
        self.swap(nums, temp, b)
        return temp, mark

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp