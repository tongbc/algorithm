# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        q = deque()
        if not root:
            return []
        q.append(root)
        length = len(q)
        while (q):
            for i in range(length):
                root = q.popleft()
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
                if i == length - 1:
                    res.append(root.val)
                    length = len(q)
        return res


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(sol.rightSideView(root))