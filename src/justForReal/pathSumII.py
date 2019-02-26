# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        target = sum
        sum = 0
        part = []
        res = []
        if not root:
            return []

        self.partSum(root, sum, part, res, target)
        return res

    def partSum(self, root, sum, part, res, target):

        if not root.left and not root.right and (sum + root.val) == target:
            part.append(root.val)
            res.append(part)
        if root.left:
            self.partSum(root.left, sum + root.val, part + [root.val], res, target)
        if root.right:
            self.partSum(root.right, sum + root.val, part + [root.val], res, target)