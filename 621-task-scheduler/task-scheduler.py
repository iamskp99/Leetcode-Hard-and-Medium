import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        # max heap (negative values)
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown = deque()  # (ready_time, remaining_count)

        while max_heap or cooldown:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap)
                cnt += 1  # reduce count

                if cnt != 0:
                    cooldown.append((time + n, cnt))

            # bring back tasks whose cooldown is over
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(max_heap, cooldown.popleft()[1])

        return time