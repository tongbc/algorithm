class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lis = []
        for i in range(n):
            num = i+1
            if (num%15==0):
                lis.append("FizzBuzz")
            elif(num%5==0):
                lis.append("Buzz")
            elif(num%3==0):
                lis.append("Fizz")
            else:
                lis.append(str(i+1))
        return lis

    # return [str(i) if (i % 3 != 0 and i % 5 != 0) else (('Fizz' * (i % 3 == 0)) + ('Buzz' * (i % 5 == 0))) for i in
    #         range(1, n + 1)]
