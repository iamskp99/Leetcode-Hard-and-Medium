import sys
sys.setrecursionlimit(2*(10**5))
class Solution:
    def rec(self,node,parent):
        e = set()
        gg = 0
        som = 0
        for x in self.d[node]:
            if x == parent:
                continue

            rr = self.rec(x,node)
            som += rr
            gg = rr
            e.add(rr)

        if len(e) == 1 or len(e) == 0:
            self.ans += 1

        return 1+som

    def countGoodNodes(self, edges: List[List[int]]) -> int:
        self.d = {}
        for x in edges:
            u,v = x[0],x[1]
            if u in self.d:
                self.d[u].append(v)

            else:
                self.d[u] = [v]

            if v in self.d:
                self.d[v].append(u)
            
            else:
                self.d[v] = [u]

        self.visited = set()
        self.ans = 0
        self.rec(0,-1)
        return self.ans