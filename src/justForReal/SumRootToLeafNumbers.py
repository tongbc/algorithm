# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = deque()
        valque = deque()
        queue.append(root)
        valque.append(root.val)
        count = 0
        while queue:
            length = len(queue)

            for i in range(length):
                root = queue.popleft()
                val = valque.popleft()
                if(root.left):
                    queue.append(root.left)
                    valque.append(val*10+root.left.val)
                if(root.right):
                    queue.append(root.right)
                    valque.append(val*10+root.right.val)
                if not(root.left) and not(root.right):
                    count+=val
        return count