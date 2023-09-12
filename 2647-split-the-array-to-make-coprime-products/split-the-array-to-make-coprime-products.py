#Returns set prime factors O(nloglogn) (Pre-computation),log n per query
import math as mt
MAXN = 1000000+101
spf = [0 for i in range(MAXN)]

def sieve():
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i

    for i in range(4, MAXN, 2):
        spf[i] = 2

    for i in range(3, mt.ceil(mt.sqrt(MAXN))):
        if (spf[i] == i):
            for j in range(i * i, MAXN, i):
                if (spf[j] == j):
                    spf[j] = i

def getFactorization(x):
    ret = []
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]

    return ret

sieve()

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        l = [0 for i in range((10**6)+1)]
        for x in nums:
            o = getFactorization(x)
            for e in o:
                l[e] += 1

        count = set()
        s = set()
        for i in range(n-1):
            x = nums[i]
            o = getFactorization(x)
            for e in o:
                s.add(e)
                l[e] -= 1
                if l[e] == 0:
                    count.add(e)

            if len(count) == len(s):
                return i

        return -1
