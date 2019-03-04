class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        temp = ""
        left, right = n, n
        res = []
        self.part(left, right, temp, res)
        return res

    def part(self, left, right, temp, res):
        if (right == 0):
            res.append(temp)
        if (right > left):
            self.part(left, right - 1, temp + ")", res)
        if (left > 0):
            self.part(left - 1, right, temp + "(", res)