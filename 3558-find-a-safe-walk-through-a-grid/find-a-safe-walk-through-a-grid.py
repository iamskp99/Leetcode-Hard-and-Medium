from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n = len(grid)
        m = len(grid[0])

        # Deque for 0-1 BFS
        queue = deque([(0, 0)])  
        dist = [[float('inf')] * m for _ in range(n)]  # Distance array
        dist[0][0] = grid[0][0]  # Starting point distance
        
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Check if within grid bounds
                if 0 <= nx < n and 0 <= ny < m:
                    new_cost = dist[x][y] + grid[nx][ny]

                    # Only proceed if the new cost is better than the previous recorded cost
                    if new_cost < dist[nx][ny] and new_cost < health:
                        dist[nx][ny] = new_cost

                        # Push to front if the move is "free" (cost 0), otherwise push to back
                        if grid[nx][ny] == 0:
                            queue.appendleft((nx, ny))
                        else:
                            queue.append((nx, ny))
                        
                        # Early exit if we reach the bottom-right corner within the health limit
                        if nx == n - 1 and ny == m - 1:
                            return True

        # Check if we reached the bottom-right corner within the health limit
        return dist[n-1][m-1] < health
