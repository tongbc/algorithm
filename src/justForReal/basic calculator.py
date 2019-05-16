class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result, number, sign = 0, 0, 1
        for n in s:
            if n.isdigit():
                number = number * 10 + int(n)
            else:
                if n == "+":
                    result += sign * number
                    number = 0
                    sign = 1
                if n == "-":
                    result += sign * number
                    number = 0
                    sign = -1
                if n == "(":
                    stack.append(result)
                    stack.append(sign)
                    result = 0
                    sign = 1
                if n == ")":
                    result = number * sign + result
                    number = 0
                    result *= stack.pop()
                    result += stack.pop()
        if (number != 0): result += sign * number
        return result
