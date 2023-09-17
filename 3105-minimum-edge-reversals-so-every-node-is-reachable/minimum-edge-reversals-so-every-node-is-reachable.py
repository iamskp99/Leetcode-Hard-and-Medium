import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class Solution:
    def rec(self,i):
        cur = 0
        self.visited.add(i)
        if i in self.d:
            for j in self.d[i]:
                if j not in self.visited:
                    som = self.rec(j)
                    cur += som

        if i in self.h:
            for j in self.h[i]:
                if j not in self.visited:
                    som = self.rec(j)
                    cur += (som+1)

        self.l[i] = cur
        return cur
    
    def helper(self,i,p,w):
        som = 0
        if p != -1:
            rr = 1
            if w:
                rr = 0
                som += 1

            som += (self.ans[p]-(self.l[i]+rr))

        som += self.l[i]
        self.ans[i] = som
        self.visited.add(i)
        if i in self.d:
            for j in self.d[i]:
                if j not in self.visited:
                    self.helper(j,i,1)

        if i in self.h:
            for j in self.h[i]:
                if j not in self.visited:
                    self.helper(j,i,0)

        return
        

    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        d = {}
        h = {}
        s = set()
        for x in edges:
            u,v = x[0],x[1]
            s.add(v)
            if u in d:
                d[u].append(v)

            else:
                d[u] = [v]

            if v in h:
                h[v].append(u)

            else:
                h[v] = [u]

        self.d,self.h = d,h
        self.l = []
        self.ans = []
        num = -1
        for i in range(n):
            self.l.append(0)
            self.ans.append(0)
            if i not in s:
                num = i

        self.visited = set()
        self.rec(num)
        # print(num)
        # print(self.l)
        self.num = num
        self.visited = set()
        self.helper(num,-1,-1)
        return self.ans