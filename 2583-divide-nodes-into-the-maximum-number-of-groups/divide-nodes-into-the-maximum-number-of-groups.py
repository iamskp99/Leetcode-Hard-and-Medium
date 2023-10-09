from collections import deque
class Solution:
    def bfs(self,x):
        queue = deque([x])
        level = {x:1}
        now = 1
        while len(queue) > 0:
            ele = queue.popleft()
            cur = level[ele]
            if ele not in self.d:
                continue

            for node in self.d[ele]:
                if node in level:
                    if abs(level[node]-cur) != 1:
                        return -1

                    continue

                level[node] = cur+1
                now = max(now,cur+1)
                queue.append(node)

        return now

    def make_groups(self,n):
        w = []
        visited = set()
        for i in range(1,n+1):
            if i in visited:
                continue

            queue = deque([i])
            explored = []
            visited.add(i)
            while len(queue) > 0:
                ele = queue.popleft()
                explored.append(ele)
                if ele not in self.d:
                    continue

                for node in self.d[ele]:
                    if node in visited:
                        continue

                    visited.add(node)
                    queue.append(node)

            w.append(explored)

        return w

    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        d = {}
        for x in edges:
            u,v = x[0],x[1]
            if u in d:
                d[u].append(v)

            else:
                d[u] = [v]

            if v in d:
                d[v].append(u)

            else:
                d[v] = [u]

        self.d = d
        ans = 0
        w = self.make_groups(n)
        print(w)
        for l in w:
            gg = -1
            for i in l:
                cur = self.bfs(i)
                gg = max(cur,gg)

            if gg == -1:
                return -1
            
            ans += gg

        return ans