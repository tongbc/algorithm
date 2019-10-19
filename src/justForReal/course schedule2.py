class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = collections.defaultdict(list)
        dic = dict((n,0) for n in range(numCourses))
        for u,v in prerequisites:
            dic[u]+=1
            G[v].append(u)
        zero = [i for i in dic if dic[i]==0]
        if not zero:
            return []
        res = []
        while(zero):
            p = zero.pop()
            res.append(p)
            for v in G[p]:
                dic[v]-=1
                if dic[v]==0:
                    zero.append(v)
        if len(res)!=numCourses:
            return []
        return res