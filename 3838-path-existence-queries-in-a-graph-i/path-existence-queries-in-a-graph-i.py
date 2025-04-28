class Union():
    def __init__(self,parent,rank):
        self.parent = parent
        self.rank = rank

    def union(self, a, b):
        e1 = self.findp(a)
        e2 = self.findp(b)
        if e1 == e2:
            return e1

        if self.rank[e1] < self.rank[e2]:
            self.parent[e1] = self.parent[e2]
            return e2

        elif self.rank[e1] > self.rank[e2]:
            self.parent[e2] = self.parent[e1]
            return e1

        else:
            self.parent[e1] = self.parent[e2]
            self.rank[e1] += 1
            return e2

    def findp(self, a):
        if self.parent[a] == a:
            return a

        self.parent[a] = self.findp(self.parent[a])
        return self.parent[a]

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parent,rank = [],[]
        for i in range(n+1):
            parent.append(i)
            rank.append(0)

        obj = Union(parent,rank)

        i,j = 0,0
        while i < n and j < n:
            if abs(nums[i]-nums[j]) <= maxDiff:
                obj.union(i,j)
                j += 1
            else:
                i += 1
            
        ans = []
        for ele in queries:
            x,y = ele
            if obj.findp(x) == obj.findp(y):
                ans.append(True)
            else:
                ans.append(False)

        return ans

