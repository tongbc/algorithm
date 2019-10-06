def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0
    if " " in s:
        return 1
    letters = [-1]*26
    res = [0]*len(s)
    letters[ord(s[0])-ord("a")] = 0
    res[0] = 1
    for i in range(1,len(s)):
        num = ord(s[i])-ord("a")
        if letters[num]==-1 or i-letters[num]>res[i-1]:
            res[i]=res[i-1]+1
            letters[num]=i
        else:
            res[i] = i-letters[num]
            letters[num]=i
    return max(res)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        res = 0
        start = 0
        for i,v in enumerate(s):
            if v in used and start<=used[v]:
                start = used[v]+1
            else:
                res = max(res,i-start+1)
            used[v] = i
        return res
print(lengthOfLongestSubstring("pwwkew"))