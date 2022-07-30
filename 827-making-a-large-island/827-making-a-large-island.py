import sys
input = sys.stdin.readline
from collections import deque
class Solution:
    def bfs(self,start):
        cnt = 0
        queue = deque([start])
        self.explored = {(start)}
        while len(queue) > 0:
            e = queue.popleft()
            cnt += 1
            i,j = e[0],e[1]
            o = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            for x in o:
                if x[0] < 0 or x[0] >= self.n or x[1] < 0 or x[1] >= self.m:
                    continue
                    
                if self.grid[x[0]][x[1]] == 1:
                    if x not in self.explored:
                        queue.append(x)
                        self.explored.add(x)
        
        return cnt
    
    
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.n,self.m = len(grid),len(grid[0])                        
        self.ans = 0
        self.visited = set()
        self.grid = grid
        self.d = {}
        self.t = {}
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    e = (i,j)
                    self.explored = set()
                    if e not in self.visited:
                        rr = self.bfs(e)
                        for y in self.explored:
                            self.d[y] = rr
                            self.t[y] = e
                            self.visited.add(y)
                            
                        self.ans = max(self.ans,rr)
                        self.visited.add(e)
                        
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 0:
                    cnt = 1
                    o = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
                    ee = set()
                    for x in o:
                        if x[0] < 0 or x[0] >= self.n or x[1] < 0 or x[1] >= self.m:
                            continue
                            
                        if grid[x[0]][x[1]] == 0:
                            continue
                        
                        q = self.t[x]
                        if q in ee:
                            continue
                        
                        ee.add(q)
                        if q in self.d:
                            cnt += self.d[q]
                        
                    self.ans = max(self.ans,cnt)
        
        return self.ans