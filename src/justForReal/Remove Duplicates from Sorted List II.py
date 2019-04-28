# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dumb = ListNode(0)
        pre = dumb
        one = head
        dumb.next = head
        while (head):
            flag = 0
            while (head.next and head.next.val == one.val):
                flag = 1
                head = head.next
                one = one.next
            if flag:
                pre.next = head.next
                one = one.next
                head = head.next
            else:
                pre = pre.next
                head = head.next
                one = one.next
        return dumb.next

