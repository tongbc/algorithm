# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#binary search solution
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return
        count = self.countNum(root.left)
        if (k <= count):
            return self.kthSmallest(root.left, k)
        elif (k > count + 1):
            return self.kthSmallest(root.right, k - 1 - count)
        return root.val

    def countNum(self, root):
        if not root:
            return 0
        else:
            return 1 + self.countNum(root.left) + self.countNum(root.right)
#dfs
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)