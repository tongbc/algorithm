import itertools
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        dic = {}
        for lis in allowed:
            temp = lis[:2]
            try:
                dic[temp] += [lis[2]]
            except KeyError:
                dic[temp] = [lis[2]]

        def dfs(bottom):
            if len(bottom) == 2 and bottom in dic:
                return True
            options = []
            for i in range(len(bottom) - 1):
                if bottom[i:i + 2] in dic:
                    options.append(dic[bottom[i:i + 2]])
                else:
                    return False
            for bot in itertools.product(*options):
                if dfs("".join(bot)):
                    return True
            return False

        return dfs(bottom)
