import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = [0 for i in range(26)]
        for ele in tasks:
            c[ord(ele)-65] += 1

        # h = [(1,-i) for i in c]
        h = []
        for q in c:
            if q == 0:
                continue
            h.append((1,-q))

        heapq.heapify(h)
        ans = 1
        while len(h) > 0:
            # print(h,ans)
            c,f = h[0]
            if c > ans:
                ans += 1
                continue
            heapq.heappop(h)
            f += 1
            ans += 1
            if f == 0:
                continue

            c += (n+1)
            heapq.heappush(h,(c,f))

        return ans-1