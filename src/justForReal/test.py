class Solution(object):
    def canCompleteCircuit(self):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        num = 5
        l = 4
        print(self.cut(num,l))

    def cut(self, num, length):
        if num > length:
            return num - length
        return num

temp = Solution()
temp.canCompleteCircuit()