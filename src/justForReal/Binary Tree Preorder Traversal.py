# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        lis = []
        cur = root
        while cur or lis:
            if cur:
                res.append(cur.val)
                lis.append(cur.right)
                cur = cur.left
            else:
                cur = lis.pop()
        return res