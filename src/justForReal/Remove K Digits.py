# class Solution(object):
#     def removeKdigits(self, num, k):
#         """
#         :type num: str
#         :type k: int
#         :rtype: str
#         """
#
#         while(k>0):
#             k-=1
#             i=0
#             while(i<len(num)-1):
#                 if num[i]>num[i+1]:
#                     break
#                 i+=1
#             num = num[:i]+num[i+1:]
#         if len(num) ==0:
#             return "0"
#         else:
#             return str(int(num))
#

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for idx in range(len(num)):
            while stack and k > 0:
                if num[idx] < stack[-1]:
                    k -= 1
                    stack.pop()
                else:
                    break
            stack.append(num[idx])
        while (k != 0):
            stack.pop()
            k -= 1
        while stack:
            if stack[0] == '0':
                stack = stack[1:]
            else:
                break

        return ''.join(stack) or '0'
sol = Solution()
num = "1432219"
k = 3
sol.removeKdigits(num,k)