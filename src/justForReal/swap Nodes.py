# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        self.part(dummy)
        return dummy.next

    def part(self, pre):
        if pre.next and pre.next.next:
            last = pre.next.next.next
            p, q = pre.next, pre.next.next
            pre.next = q
            p.next = last
            q.next = p
            self.part(p)
        else:
            return
