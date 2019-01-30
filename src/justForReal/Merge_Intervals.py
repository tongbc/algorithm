#
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        out = []
        for i in sorted(intervals,key = lambda i:i.start):
            if out and i.start<=out[-1].end:
                out[-1].end = max(i.end,out[-1].end)
            else:
                out.append(i)
        return out