# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dfs(root)[0],self.dfs(root)[1])
    def dfs(self,root):
        if not root:
            return [0,0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        res = [0,0]
        res[0] = left[1]+right[1] + root.val
        res[1] = max(left[1],left[0]) + max(right[1],right[0])
        return res
