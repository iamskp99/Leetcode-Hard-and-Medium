from collections import deque
class Solution:
    def bfs(self,start,grid,visited):
        queue = deque([start])
        n,m = len(grid),len(grid[0])
        res_found = False
        while len(queue) > 0:
            x = queue.popleft()
            l = [(0,-1),(0,1),(-1,0),(1,0)]
            for ele in l:
                nx,ny = x[0]+ele[0],x[1]+ele[1]
                if nx < 0 or ny < 0 or nx == n or ny == m:
                    res_found = True
                    continue
                if (nx,ny) in visited:
                    continue
                if grid[nx][ny]:
                    continue
                visited.add((nx,ny))
                queue.append((nx,ny))
        if res_found:
            return 0
        return 1
            

    def closedIsland(self, grid: list[list[int]]) -> int:
        visited = set()
        n,m = len(grid),len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if (i,j) in visited:
                    continue
                if not grid[i][j]:
                    ans += self.bfs((i,j),grid,visited)
        return ans