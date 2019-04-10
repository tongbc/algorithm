class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.in_stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self.remove()
        return self.out.pop()

    def peek(self):
        """
        Get the top element.
        :rtype: int
        """
        self.remove()
        return self.out[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.out) == 0 and len(self.in_stack) == 0

    def remove(self):
        if not self.out:
            while (len(self.in_stack) > 0):
                self.out.append(self.in_stack.pop())

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()