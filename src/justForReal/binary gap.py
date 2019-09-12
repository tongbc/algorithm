class Solution:
    def binaryGap(self, N: int) -> int:
        pre,dis = 0,0
        for i,num in enumerate(bin(N)[2:]):
            if num == "1":
                dis = max(dis,i-pre)
                pre = i
        return dis