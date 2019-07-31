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
        df = [False]*(len(s)+1)
        df[0] = True
        for i in range(len(s)):
            for w in words:
                if i-len(w)+1>=0 and w==s[i-len(w)+1:i+1] and df[i-len(w)+1]:
                    df[i+1] = True
        return df[len(s)]