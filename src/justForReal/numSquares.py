import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        lst = [i**2 for i in range(1,int(math.sqrt(n)+1))]
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x==y:
                        return cnt
                    if x<y:
                        break
                    temp.add(x-y)
            toCheck = temp
        return cnt