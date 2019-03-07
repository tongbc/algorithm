class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res1, res2 = -1, -1
        low, high = 0, len(nums) - 1
        while (low <= high):
            mid = (low + high) // 2
            if ((mid - 1) == -1 and nums[mid] == target) or (nums[mid] == target and nums[mid - 1] < target):
                res1 = mid
                break
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] >= target:
                high = mid - 1

        low, high = 0, len(nums) - 1
        while (low <= high):
            mid = (low + high) // 2
            if ((mid + 1) == len(nums) and nums[mid] == target) or (nums[mid] == target and nums[mid + 1] > target):
                res2 = mid
                break
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] <= target:
                low = mid + 1
        return [res1, res2]


sol = Solution()
nums = [5,7,7,8,8,10]
print(sol.searchRange(nums,8))