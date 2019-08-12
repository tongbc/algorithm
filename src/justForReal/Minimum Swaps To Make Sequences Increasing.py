class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        swap,not_swap = [len(A)]*len(A),[len(A)]*len(A)
        swap[0],not_swap[0] = 1,0
        for i in range(1,len(A)):
            if A[i]>A[i-1] and B[i]>B[i-1]:
                not_swap[i] = not_swap[i-1]
                swap[i] = swap[i-1]+1
            if A[i]>B[i-1] and B[i]>A[i-1]:
                swap[i] = min(swap[i],not_swap[i-1]+1)
                not_swap[i] = min(not_swap[i],swap[i-1])
        return min(not_swap[-1],swap[-1])