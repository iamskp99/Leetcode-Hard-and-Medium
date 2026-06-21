from collections import deque
class Solution:
    def check(self,u,v):
        cnt = 0
        for i in range(len(u)):
            if u[i] != v[i]:
                cnt += 1

        if cnt == 1:
            return True
        return False

    def bfs(self,start,end,graph):
        queue = deque([start])
        visited = {start}
        mp = {start:0}
        while len(queue) > 0:
            ele = queue.popleft()
            for item in graph[ele]:
                if item not in visited:
                    mp[item] = mp[ele]+1
                    queue.append(item)
                    visited.add(item)

        ans = []
        def dfs(i,o):
            if i == start:
                ans.append(o[::-1])
                return

            for ele in graph[i]:
                if ele in mp and mp[ele]+1 == mp[i]:
                    o.append(ele)
                    dfs(ele,o)
                    o.pop()
            return

        if end not in mp:
            return []

        dfs(end,[end])
        return ans

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        if beginWord not in wordList: 
            w = [beginWord]+wordList
        else:
            w = wordList

        d,n = {},len(w)
        for ew in w:
            d[ew] = []
        for i in range(n):
            for j in range(i+1,n):
                u,v = w[i],w[j]
                if not self.check(u,v):
                    continue

                if u in d:
                    d[u].append(v)
                else:
                    d[u] = [v]

                if v in d:
                    d[v].append(u)
                else:
                    d[v] = [u]

        return self.bfs(beginWord,endWord,d)

                