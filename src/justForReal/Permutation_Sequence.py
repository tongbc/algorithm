import math
def getPermutation(n, k):
    array = list(range(1, n + 1))
    k = (k % math.factorial(n)) - 1
    permutation = []
    for i in range(n - 1, -1, -1):
        idx, k = divmod(k, math.factorial(i))
        permutation.append(array.pop(idx))

    return "".join(map(str, permutation))

print(getPermutation(3,3))