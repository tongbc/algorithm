# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number ==0:
            return 0
        if number==1:
            return 1
        if number==2:
            return 2
        res = [0]*number
        res[0],res[1] = 1,2
        for i in range(2,number):
            res[i] = res[i-1]+res[i-2]
        return res[number-1]