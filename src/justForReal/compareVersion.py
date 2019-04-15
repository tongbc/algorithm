class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        a = version1.split(".")
        b = version2.split(".")
        a = [int(x) for x in a]
        b = [int(x) for x in b]
        len1 = len(a)
        len2 = len(b)
        maxLen = max(len1, len2)
        lis1 = [0] * maxLen
        lis2 = [0] * maxLen
        lis1[:len1] = a
        lis2[:len2] = b
        for i in range(maxLen):
            if (lis1[i] > lis2[i]):
                return 1
            elif (lis1[i] < lis2[i]):
                return -1
        return 0

