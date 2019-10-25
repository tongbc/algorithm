class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        lis = sorted(intervals)
        res = [lis[0]]
        l,r = lis[0][0],lis[0][1]
        for a,b in lis[1:]:
            if a>r:
                res.append([a,b])
                l,r = a,b
            elif  b>r:
                res[-1] = [l,b]
                r = b
            else:
                continue
        return res