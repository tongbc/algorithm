# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res = []
        self.part(root.left,res)
        res.append(root.val)
        self.part(root.right,res)
        m = 0xfffffff
        for i in range(len(res)-1):
            m= min(m,res[i+1]-res[i])
        return m
    def part(self,root,res):
        if not root:
            return
        self.part(root.left,res)
        res.append(root.val)
        self.part(root.right,res)