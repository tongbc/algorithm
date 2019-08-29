# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def deep(root):
            if not root:return 0,None
            l,r = deep(root.left),deep(root.right)
            if l[0]>r[0]:return l[0]+1,l[1]
            elif r[0]>l[0]:return r[0]+1,r[1]
            else:return l[0]+1,root
        return deep(root)[1]