# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.getD(root.left)
        right = self.getD(root.right)
        if left == right:
            return pow(2, left) + self.countNodes(root.right)
        else:
            return pow(2, right) + self.countNodes(root.left)

    def getD(self, root):
        if not root:
            return 0
        num = 0
        return 1 + self.getD(root.left)