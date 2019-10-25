class Solution(object):
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    def parent(self,i):
        return (i-2)>>1
    def max_heapify(self,nums,i):
        l,r = self.left(i),self.right(i)
        if l<len(nums) and nums[l]>nums[i]:
            largest = l
        else:
            largest = i
        if r<len(nums) and nums[r]>nums[largest]:
            largest = r
        if largest!=i:
            self.swap(nums,i,largest)
            self.max_heapify(nums,largest)
    def build_max_heap(self,nums):
        for i in range((len(nums)-2)>>1,-1,-1):
            self.max_heapify(nums,i)
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    def pop_max(self,nums):
        num = nums[0]
        nums[0] = nums[-1]
        nums = nums[:len(nums)-1]
        self.max_heapify(nums, 0)
        print(nums)
        return(num,nums)

sol = Solution()
lis = [3,5,7,2]
sol.build_max_heap(lis)
m,nums = sol.pop_max(lis)
print(nums)
# print(4>>1)
# print(lis[:len(lis)-1])