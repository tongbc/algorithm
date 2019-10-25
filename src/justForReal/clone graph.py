# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return 
        n_copy = Node(node.val,[])
        dic = {}
        dic[node] = n_copy
        stack = [node]
        while(stack):
            v = stack.pop()
            for neighbor in v.neighbors:
                if neighbor not in dic:
                    n_copy = Node(neighbor.val,[])
                    dic[neighbor] = n_copy
                    dic[v].neighbors.append(n_copy)
                    stack.append(neighbor)
                else:
                    dic[v].neighbors.append(dic[neighbor])
        return dic[node]