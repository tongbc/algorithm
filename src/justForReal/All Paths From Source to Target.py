class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        def dfs(cur, path):
            if cur == len(graph) - 1:
                res.append(path)
            else:
                for i in graph[cur]:
                    dfs(i, path + [i])

        res = []
        dfs(0, [0])
        return res

    def dfs(self, cur, path):
        if cur == len(graph) - 1:
            res.append(path)
        else:
            for i in graph[cur]:
                self.dfs(i, path + [i])
