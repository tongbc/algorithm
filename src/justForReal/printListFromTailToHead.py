class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        p = None
        q,nxt = listNode,listNode
        while(q.next):
            nxt = q.next
            q.next = p
            p = q
            q = nxt
        q.next = p
        head = q
        res = []
        while(head):
            res.append(head.val)
            head = head.next
        return res

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
sol = Solution()
print(sol.printListFromTailToHead(a))