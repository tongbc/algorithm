def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    res = [0] * n
    res[0] = 1
    cur = [0] * len(primes)
    for i in range(1, n):
        res[i] = 10000000000
        for j in range(len(primes)):
            if primes[j] * res[cur[j]] == res[i - 1]:
                print(primes[j],res[cur[j]])
                print(res[i - 1])
                cur[j] += 1
            res[i] = min(res[i], primes[j] * res[cur[j]])

    return res[n - 1]

primes = [2,3]
print(nthSuperUglyNumber(6,primes))