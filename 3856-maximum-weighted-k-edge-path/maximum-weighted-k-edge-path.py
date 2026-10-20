class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        d = defaultdict(list)
        for u, v, w in edges:
            d[u].append((v, w))
        q = deque([(i, 0, 0) for i in range(n)])
        ans = -1
        vis = set(q)
        while q:
            cur, l, x = q.popleft()
            if l == k:
                ans = max(ans, x)
                continue
            for v, w in d[cur]:
                new = (v, l + 1, w + x)
                if w + x < t and new not in vis:
                    q.append(new)
                    vis.add(new)
        return ans