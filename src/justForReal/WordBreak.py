class Solution(object):
    ##DFS 容易超时
    # def wordBreak(self, s, wordDict):
    #     """
    #     :type s: str
    #     :type wordDict: List[str]
    #     :rtype: bool
    #     """
    #     self.part(s, wordDict)
    #
    # def part(self, s, wordDict):
    #     if s == "":
    #         return True
    #     for word in wordDict:
    #         if str(s).startswith(str(word)):
    #             if (self.part(s[len(word):], wordDict)):
    #                 return True
    #     return False
    def wordBreak(self, s, words):
        ok = [True]
        for i in range(1, len(s) + 1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]
