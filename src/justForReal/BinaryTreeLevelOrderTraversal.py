# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue


class Solution:
    def levelOrder(self, root):
        if not root: return []
        queue, res = Queue(), []
        queue.put(root)

        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.get()
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
                cur_level.put(node.val)
            res.append(cur_level)
        return res