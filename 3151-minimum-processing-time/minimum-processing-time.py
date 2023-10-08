import heapq
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        l = []
        for i in processorTime:
            l.append(i)
            l.append(i)
            l.append(i)
            l.append(i)

        tasks.sort(reverse=True)
        heapq.heapify(l)
        ans = 0
        for i in tasks:
            ele = heapq.heappop(l)
            ans = max(i+ele,ans)

        return ans