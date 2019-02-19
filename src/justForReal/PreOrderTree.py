class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preOrderTraversal(root):
    stack = []
    res = []
    cur = root
    while root or stack:
        if root:
            res.append(cur)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()
    return res