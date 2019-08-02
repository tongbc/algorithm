class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(S)-1,-1,-1):
            if S[i] not in dic:
                dic[S[i]] = i
        start,end = 0,0
        res = []
        for index,s in enumerate(S):
            if dic[s]>end:
                end = dic[s]
            if end==index:
                res.append(end-start+1)
                start,end = index+1,index+1
        return res