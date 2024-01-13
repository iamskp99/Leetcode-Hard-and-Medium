import sys
input = sys.stdin.readline

#Returns set prime factors O(nloglogn) (Pre-computation),log n per query
import math as mt
MAXN = 100000+101
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
    ret = set()
    while (x != 1):
        ret.add(spf[x])
        x = x // spf[x]

    return ret

class Solution:
    def findParent(self,x):
        while self.parent[x] != x:
            x = self.parent[x]

        return x

    def merge(self,x,y):
        p1 = self.findParent(x)
        p2 = self.findParent(y)
        if p1 == p2:
            return 

        if self.rank[p1] == self.rank[p2]:
            self.rank[p2] += 1
            self.parent[p1] = p2
            return 

        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
            return 

        if self.rank[p2] < self.rank[p1]:
            self.parent[p2] = p1
            return

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        self.parent = []
        self.rank = []
        for i in range(100002):
            self.parent.append(i)
            self.rank.append(0)

        if spf[2] != 2:
            sieve()

        d = {}
        one_count = 0
        for i in nums:
            l = getFactorization(i)
            if i == 1:
                one_count += 1

            for x in l:
                if x in d:
                    d[x].add(i)

                else:
                    d[x] = {i}

        if one_count > 1:
            return False

        for item in d:
            l = d[item]
            ele = None
            for rr in l:
                ele = rr
                break

            l.remove(ele)
            for j in l:
                self.merge(ele,j)
            
        parents = set()
        for i in nums:
            parents.add(self.findParent(i))

        if len(parents) == 1:
            return True

        return False

        

        