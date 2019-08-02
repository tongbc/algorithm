class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if not answers:
            return 0
        dic = {}
        for num in answers:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1
        sum = 0
        for key,value in dic.items():
            if key==0:
                sum+=value
            else:
                if key<value:
                    while(key<value):
                        sum += (key+1)
                        value = value-key-1
                    if value!=0:
                        sum+=(1+key)
                else:
                    sum +=(1+key)
        return sum