# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# ulr lur  lru->url
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur.left)
                res.append(cur.val)
                cur = cur.right
            else:
                cur = stack.pop()
        return res[::-1]