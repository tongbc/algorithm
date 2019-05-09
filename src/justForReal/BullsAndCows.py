class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        dic1 = [0] * 10
        dic2 = [0] * 10
        a, b = 0, 0
        for i,j in zip(secret,guess):
            i = int(i)
            j = int(j)
            if i==j:
                a += 1
            else:
                dic1[i] += 1
                dic2[j] += 1
        for i in range(10):
            i = int(i)
            if dic2[i] == 0:
                continue
            b += dic1[i] if dic2[i] >= dic1[i] else dic2[i]
        return str(a) + "A" + str(b) + "B"