def solve(N, K, nums):
    s = str(nums)
    lis = [1]*len(s)
    for i in range(len(s)-K+1):
        lis[i] = int(s[:i+1])
    for i in range(1,K):
        for j in range(i,len(s)-K+i+1):
            print(lis[0],int(s[1:j+1]))
            lis[j] = max([lis[k]*int(s[k+1:j+1]) for k in range(i-1,j)])
    m = -10000
    for k in range(K, len(s)):
        m = max(lis[k - 1] * int(s[k:len(s)]), m)
        print(lis[k - 1], s[k:len(s)])
    return m
print(solve(4,3,5341))
# N, K = map(int, input().strip().split(" "))
# nums = input().strip()
# res = solve(N, K, nums)
# print(res)
# s = "123"
# print(s[1:2])
# lis = [2,3,5]
# print(max([k*2 for k in lis]))