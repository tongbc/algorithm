class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        q = deque()
        q.append(root)
        l = len(q)
        while(q):
            for i in range(l):
                p = q.popleft()
                if i==l-1:
                    p.next = None
                else:
                    p.next = q[0]
                if p.left:
                    q.append(p.left)
                if(p.right):
                    q.append(p.right)
            l = len(q)
        return root

node4 = Node(4,None,None,None)
node5 = Node(5,None,None,None)
node6 = Node(6,None,None,None)
node7 = Node(7,None,None,None)

node2 = Node(2,node4,node5,None)
node3 = Node(3,node6,node7,None)
node1 = Node(1,node2,node3,None)
sol = Solution()
root = sol.connect(node1)
print(root)
