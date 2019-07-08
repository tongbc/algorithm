## 1 not in place
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # nums = sorted(nums)
        # half = len(nums[::2])
        # nums[::2],nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

## 2
# public void wiggleSort(int[] nums) {
#     int median = findKthLargest(nums, (nums.length + 1) / 2);
#     int n = nums.length;
#
#     int left = 0, i = 0, right = n - 1;
#
#     while (i <= right) {
#
#         if (nums[newIndex(i,n)] > median) {
#             swap(nums, newIndex(left++,n), newIndex(i++,n));
#         }
#         else if (nums[newIndex(i,n)] < median) {
#             swap(nums, newIndex(right--,n), newIndex(i,n));
#         }
#         else {
#             i++;
#         }
#     }
#
#
# }
#
# private int newIndex(int index, int n) {
#     return (1 + 2*index) % (n | 1);
# }