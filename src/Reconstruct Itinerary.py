import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        dic = collections.defaultdict(list)
        for a,b in sorted(tickets)[::-1]:
            dic[a].append(b)
        res = []
        def visit(a):
            while(dic[a]):
                visit(dic[a].pop())
            res.append(a)
        visit("JFK")
        return res[::-1]