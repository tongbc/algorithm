class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n==1:
            return [0]
        adj = [set() for _ in range(n)]
        for i,j in edges:
            adj[i].add(j)
            adj[j].add(i)
        leaves = [i for i in range(n) if len(adj[i])==1]
        while(n>2):
            n-=len(leaves)
            new_leaves = []
            for v in leaves:
                j = adj[v].pop()
                adj[j].remove(v)
                if len(adj[j])==1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves