from collections import deque

def bfs(start,graph):
    queue = deque([start])
    visited = {start}
    explored = set()
    while len(queue) > 0:
        node = queue.popleft()
        explored.add(node)
        for neighbour in graph.get(node,[]):
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

    return explored

def check(start,graph,explored,visited):
    queue = deque([start])
    visited.add(start)
    while len(queue) > 0:
        node = queue.popleft()
        for neighbour in graph.get(node,[]):
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

            if neighbour in explored:
                return False

    return True


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = {}
        for x in invocations:
            u,v = x[0],x[1]
            if u in graph:
                graph[u].append(v)

            else:
                graph[u] = [v]

        explored = bfs(k,graph)
        visited,flag = set(),False
        for i in range(n):
            if i in explored:
                continue

            if i in visited:
                continue

            if check(i,graph,explored,visited):
                continue

            else:
                flag = True

        if flag:
            return [i for i in range(n)]

        else:
            ans = []
            for i in range(n):
                if i not in explored:
                    ans.append(i)

            return ans

            
