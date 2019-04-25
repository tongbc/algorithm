# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        helper = ListNode(0) ##dummy node
        cur = head
        pre = helper
        next = None
        while(cur):
            next = cur.next
            while(pre.next is not None and pre.next.val<cur.val):
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = helper
            cur = next
        return helper.next