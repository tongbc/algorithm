def summaryRanges(nums):
    ranges = []
    for n in nums:
        if not ranges or n > ranges[-1][-1] + 1:
            ranges += [],
        ranges[-1][1:] = n,
    print(ranges)
    return ['->'.join(map(str, r)) for r in ranges]

lis = [0,1,2,4,5,7]
print(summaryRanges(lis))