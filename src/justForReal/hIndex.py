class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        buc = [0] * (length + 1)
        for num in citations:
            if num >= length:
                buc[length] += 1
            else:
                buc[num] += 1
        count = 0
        for i in range(length, -1, -1):
            count += buc[i]
            if count >= i:
                return i
        return 0
