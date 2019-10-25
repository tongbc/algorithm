import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =[]
        dic = collections.defaultdict(list)
        for word in strs:
            num = 0
            for l in word:
                num+=10**(ord(l)-ord("a"))
            dic[num].append(word)
        for key in dic:
            res.append(dic[key])
        return res

import  collections
class Solution:
    def groupAnagrams(self, strs):

        dic = collections.defaultdict(list)
        for string in strs:
            dic[''.join(sorted(string))] += [string]

        return [value for key, value in dic.items()]