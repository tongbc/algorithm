# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        lis = s.split(" ")
        res = ""
        n = len(lis)
        for a in lis[:n-1]:
            res=res+a+"%20"
        res+=lis[n-1]
        return res