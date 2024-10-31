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

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if spf[1] == 0:
            sieve()

        prev,ans = nums[-1],0
        flag = 0
        i = len(nums)-1
        while i > -1:
            if nums[i] <= prev:
                pass

            else:
                l = getFactorization(nums[i])
                l.sort()
                while len(l) > 1:
                    x = l.pop()
                    nums[i] = nums[i]//x

                if nums[i] > prev:
                    flag = 1
                    break

                ans += 1

            prev = nums[i]
            i -= 1

        return -1 if flag else ans