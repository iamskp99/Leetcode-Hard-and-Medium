import math as mt
MAXN = 1000000+101
spf = [0 for i in range(MAXN)]
M = (10**9)+7

#Fast modular exponentiation
def power(x,y):
    ans = 1
    while(y>0):
        if(y%2 == 1):
            ans = (ans*x)%M
        y = y //2
        x = (x*x)%M
    return ans%M


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
    ret = set()
    while (x != 1):
        ret.add(spf[x])
        x = x // spf[x]

    return len(ret)

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        if spf[2] != 2:
            sieve()

        l = []
        o = []
        pf,sf,ans,n = [],[],1,len(nums)
        for j in range(len(nums)):
            i = nums[j]
            x = getFactorization(i)
            l.append(x)
            o.append((i,j))
            pf.append(0)
            sf.append(0)

        o.sort()
        stack = []
        for i in range(n):
            x = l[i]
            while len(stack) > 0:
                if stack[-1][0] < x:
                    stack.pop()

                else:
                    break

            if len(stack) == 0:
                pf[i] = i+1

            else:
                ind = stack[-1][1]
                pf[i] = i-ind

            stack.append((x,i)) 

        i = n-1
        stack = []
        while i > -1:
            x = l[i]
            while len(stack) > 0:
                if stack[-1][0] <= x:
                    stack.pop()

                else:
                    break

            if len(stack) == 0:
                sf[i] = n-i

            else:
                ind = stack[-1][1]
                sf[i] = ind-i

            stack.append((x,i))
            i -= 1

        while k > 0 and len(o) > 0:
            ele = o.pop()
            x,ind = ele[0],ele[1]
            e1,e2 = pf[ind],sf[ind]
            cnt = min(e1*e2,k)
            k -= cnt
            som = power(x,cnt)
            ans = (ans*som)%M

        return ans