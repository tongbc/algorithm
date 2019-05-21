class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        return 1 + max(self.dep(pRoot.left), self.dep(pRoot.right))

    def dep(self, root):
        if not root:
            return 0
        return 1 + max(self.dep(root.left), self.dep(root.right))

