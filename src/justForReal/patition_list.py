# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def partition(head, x):
	"""
	:type head: ListNode
	:type x: int
	:rtype: ListNode
	"""
	node1 = ListNode(0)
	node2 = ListNode(0)
	p1 = node1
	p2 = node2
	while (head):
		if head.val < x:
			p1.next = head
			p1 = p1.next
		else:
			p2.next = head
			p2 = p2.next
		head = head.next
	p2.next = None
	p1.next = node2.next

	return node1.next

node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node1.next = node2
node2.next = node3
node3.next = node4

print(partition(node1,3))
