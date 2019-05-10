class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        dumb = ListNode(0)
        if not pHead1 and not pHead2:
            return
        if pHead1 and pHead2:
            if pHead1.val<pHead2.val:
                cur = pHead1
                pHead1 = pHead1.next
                dumb.next = cur
            else:
                cur = pHead2
                pHead2 = pHead2.next
                dumb.next = cur
            while(pHead1 and pHead2):
                if pHead1.val<pHead2.val:
                    cur.next = pHead1
                    cur = pHead1
                    pHead1 = pHead1.next
                else:
                    cur.next = pHead2
                    cur = pHead2
                    pHead2 = pHead2.next
        else:
            cur = dumb
        if pHead1:
            cur.next = pHead1
        if pHead2:
            cur.next = pHead2
        return dumb.next