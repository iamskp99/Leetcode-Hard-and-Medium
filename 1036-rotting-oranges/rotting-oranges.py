from collections import deque
class Solution:
    def bfs(self,grid,queue,n,m,count,visited):
        ans = 0
        # visited = set()
        while len(queue) > 0:
            i,j,t = queue.popleft()
            if grid[i][j] == 1:
                count -= 1
                ans = max(ans,t)

            neighbour = [(0,1),(0,-1),(1,0),(-1,0)]
            for item in neighbour:
                x,y = i+item[0],j+item[1]
                if x < 0 or x == n or y < 0 or y == m:
                    continue

                if (x,y) in visited:
                    continue

                if grid[x][y] == 0:
                    continue
                
                visited.add((x,y))
                queue.append((x,y,t+1))

        print(visited)
        return ans if count == 0 else -1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        n,m = len(grid),len(grid[0])
        visited = set()
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                    visited.add((i,j))

                if grid[i][j] == 1:
                    count += 1

        return self.bfs(grid,queue,n,m,count,visited)