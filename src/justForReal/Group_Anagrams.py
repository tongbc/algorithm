#49
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            temp = tuple(sorted(word))
            dic[temp] = dic.get(temp,[])+[word]
        return dic.values()

