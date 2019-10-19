class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        l = min(len(temp) for temp in strs)

        for i in range(l):
            begin = strs[0][i]
            flag = True
            for j in range(1, len(strs)):
                if begin == strs[j][i]:
                    continue
                else:
                    flag = False
                    break
            if flag:
                res = strs[0][:i + 1]
            else:
                break
        return res

