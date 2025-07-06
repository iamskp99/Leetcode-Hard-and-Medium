from collections import deque
class Solution:
    def bfs(self,indegree,d,n):
        queue = deque([])
        visited = set()
        ans = 0
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                visited.add(i)

        while len(queue) > 0:
            ele = queue.popleft()
            ans += 1
            if ele not in d:
                continue
            neighbour = d[ele]
            for item in neighbour:
                if item in visited:
                    continue

                indegree[item] -= 1
                if indegree[item] == 0:
                    visited.add(item)
                    queue.append(item)
        
        return ans

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for i in range(numCourses)]
        d = {}
        for item in prerequisites:
            u,v = item
            if u in d:
                d[u].append(v)
            else:
                d[u] = [v]
            indegree[v] += 1

        ans = self.bfs(indegree,d,numCourses)
        return True if numCourses == ans else False 
