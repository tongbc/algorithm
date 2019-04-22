class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1, len2 = len(num1), len(num2)
        res = [0] * (len1 + len2)
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                high, low = i + j + 1, i + j
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                mul += res[high]
                l, r = mul / 10, mul % 10
                res[low] += l
                res[high] = r
        sb = []
        for num in res:
            if num != 0 or len(sb) != 0:
                sb.append(num)
        result = "0" if len(sb) == 0 else "".join(str(s) for s in sb)
        return result



