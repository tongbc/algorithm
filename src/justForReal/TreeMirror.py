class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return
        if not root.left and not root.right:
            return root
        else:
            temp1,temp2 = False,False
            if root.left:
                temp1 = self.Mirror(root.left)
            if root.right:
                temp2 = self.Mirror(root.right)
            root.left = None
            root.right = None
            if temp2:
                root.left = temp2
            if temp1:
                root.right = temp1
        return root
