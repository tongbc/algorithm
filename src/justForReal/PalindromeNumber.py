class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        num = str(x)
        length = len(num)
        if length % 2 == 0 or length % 2 == 1:
            for i in range(length // 2):
                if num[i] != num[length - 1 - i]:
                    return False
            return True
        # if length % 2 == 1:
        #     for i in range(length // 2):
        #         if num[i] != num[length - 1 - i]:
        #             return False
        #     return True

