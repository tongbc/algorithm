# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        conn = collections.defaultdict(list)
        def connect(par,child):
            if  par and  child:
                conn[par.val].append(child.val)
                conn[child.val].append(par.val)
            if child.left:connect(child,child.left)
            if child.right:connect(child,child.right)
        connect(None,root)
        bfs = [target.val]
        seen = set(bfs)
        for i in range(K):
            bfs = [y for x in bfs for y in conn[x] if y not in seen]
            seen |= set(bfs)
        return bfs