# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root,lessThan = float("inf"),largerThan = float("-inf")):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.val >= lessThan or root.val <= largerThan :
            return False
        return self.isValidBST(root.left,min(root.val,lessThan),largerThan) and self.isValidBST(root.right,lessThan,max(root.val,largerThan))