class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(head):
    if not head:
        return
    p,q = head,head
    temp = None
    while(q.next):
        q = p.nextt
        p.next = temp
        q.next = p
        temp = p
        p = q
    return q