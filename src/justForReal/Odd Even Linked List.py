# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        a, b, bhead = head, head.next, head.next
        while (b.next and b.next.next):
            temp1, temp2 = b.next, b.next.next
            a.next = temp1
            temp1.next = bhead
            b.next = temp2
            a = temp1
            b = temp2
        if b.next:
            a.next = b.next
            a.next.next = bhead
            b.next = None
        return head
