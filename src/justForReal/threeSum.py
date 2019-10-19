class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a,b = i+1,len(nums)-1
            temp = -nums[i]
            while(b>a):
                if temp==(nums[b]+nums[a]):
                    # t_res = [nums[i],nums[a],nums[b]]
                    # if t_res not in res:
                    #     res.append(t_res)
                    # a+=1
                    while a < len(nums) - 1 and nums[a] == nums[a + 1]:
                        a += 1
                    while b > 0 and nums[b] == nums[b - 1]:
                        b -= 1
                    res.append([nums[i], nums[a], nums[b]])
                    a += 1
                elif temp>(nums[b]+nums[a]):
                    a+=1
                else:
                    b-=1
        return res