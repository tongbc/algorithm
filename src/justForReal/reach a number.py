## math version
import math
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target < 0:
            target = -target
        if target == 1:
            return 1
        large = math.ceil(-0.5 + math.sqrt(0.25 + 2 * target))
        temp = -0.5 + math.sqrt(0.25 + 2 * target)
        if temp == large:
            return int(large)

        num = (large * (large + 1)) / 2
        minus = num - target
        if minus % 2 == 0:
            return int(large)
        else:
            if large % 2 == 0:
                return int(large + 1)
            else:
                return int(large + 2)

## BFS TLE
# from collections import deque
# class Solution(object):
#     def reachNumber(self, target):
#         """
#         :type target: int
#         :rtype: int
#         """
#         lis = deque([0])
#         # lis = [0]
#         if target == 0:
#             return 0
#         l = 1
#         step = 1
#         while (True):
#             for i in range(l):
#                 temp = lis.popleft()
#                 if temp + step == target or temp - step == target:
#                     return step
#                 else:
#                     lis.append(temp + step)
#                     lis.append(temp - step)
#             l = len(lis)
#             step += 1

