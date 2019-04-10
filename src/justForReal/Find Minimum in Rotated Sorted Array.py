class Solution(object):
    def findMin(self, nums):
        left,right = 0,len(nums)-1
        while(left<right-1):
            mid = (left+right)//2
            if(nums[mid]>nums[rightt]):
                left = mid
            else:
                right = mid
        if(nums[left]>nums[right]):
            return nums[right]
        else:
            return nums[left]
