class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = -0xfffffff
        cha = 0xfffffff
        nums.sort()
        for i in range(len(nums) - 2):
            a, b = i + 1, len(nums) - 1
            pre = False
            while (a < b):
                temp = nums[i] + nums[a] + nums[b]
                if temp == target:
                    return target
                if temp > target:
                    # res = temp if abs(temp-target)<cha else res
                    if abs(temp - target) < cha:
                        res = temp
                        cha = abs(temp - target)
                    # b-=1
                    # break
                    b -= 1
                if temp < target:
                    # res = temp if abs(temp-target)<cha else res
                    if abs(temp - target) < cha:
                        res = temp
                        cha = abs(temp - target)
                    # b-=1
                    # break
                    a += 1
        return res

