class Solution:
    def IsContinuous(self, numbers):
        # write code here
        count = 0
        lis = set([])
        if not numbers:
            return False
        for num in numbers:
            if num==0:
                count+=1
                continue
            if num in lis:
                return False
            lis.add(num)
        mi = min(lis)
        ma = max(lis)
        return ma-mi==len(lis)-1+count or mi==ma