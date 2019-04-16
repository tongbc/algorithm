class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        sum = 0
        for i in A:
            sum +=i
        targets = [2*sum/3,sum/3]
        sum1 = 0
        for num in A:
            sum1+=num
            if(targets[-1]==sum1):
                targets.pop()
            if not(targets):
                return True
        return False