##241
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for index,i in enumerate(input):
            if i in "+-*":
                res1 = self.diffWaysToCompute(input[:index])
                res2 = self.diffWaysToCompute(input[(index+1):])
                for num1 in res1:
                    for num2 in res2:
                        res.append(self.op(num1,num2,i))
        return res
    def op(self,res1,res2,i):
        if i == "+":
            return res1+res2
        if i == "-":
            return res1-res2
        else:
            return res1*res2