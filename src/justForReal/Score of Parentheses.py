class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = [0]
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                num = stack.pop()
                stack[-1] += (1 if num==0 else 2*num)
            print(stack)
        return stack[0]