import copy
## stones[0][0]:time to eat stones[0][1]:energies stones[0][2]:decay speed
def get_largest_energy(stones):
    res = []
    for i in stones:
        temp = copy.deepcopy(stones)
        temp.remove(i)
        res.append(i[1]+dfs(temp,i))
    return max(res)


def dfs(stones,stone):
    if not stones:
        return 0
    for s in stones:
        s[1]-=stone[0]*s[2]
        if s[1]<0:
            s[1] =0
    res = []
    for i in stones:
        temp = copy.deepcopy(stones)
        temp.remove(i)
        res.append(i[1]+dfs(temp,i))
    return max(res)

T = int(input().strip())
for i in range(1, T + 1):
    N = int(input().strip())
    stones = []
    for _ in range(N):
        stone = list(map(int, input().strip().split()))
        stones.append(stone)
    y = get_largest_energy(stones)
    print("Case #{}: {}".format(i, y))