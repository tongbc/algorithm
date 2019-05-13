class Solution:
    def jumpFloorII(self, number):
        # write code here
        res = [0]*(number+1) if number>1 else[0,0,0]
        res[0] = 0
        res[1] = 1
        res[2] = 2
        if number<=2:
            return res[number]
        for i in range(3,number+1):
            res[i] = sum(res[:i])+1
        return res[number]