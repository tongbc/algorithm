class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = []
        cur = ""
        self.dfs(s, t, cur, res)
        e = sorted(s, key=lambda x: len(x))
        return e[0]

    def dfs(self, s, t, cur, res):
        if not t:
            res.append(cur)
        if not s:
            return
        print(s+"------"+t)
        if s[0] == t[0]:
            self.dfs(s[1:], t[1:], cur + s[0], res)
        else:
            self.dfs(s[1:], t[0:], cur, res)

sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
sol.minWindow(s,t)