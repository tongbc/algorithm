class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def postorderTraversal(self, root): ## 后序遍历
    stack = []
    sol = []
    curr = root
    while stack or curr:
        if curr:
            sol.append(curr.val)
            stack.append(curr.left)
            curr = curr.right
        else:
            curr = stack.pop()
    return sol[::-1]