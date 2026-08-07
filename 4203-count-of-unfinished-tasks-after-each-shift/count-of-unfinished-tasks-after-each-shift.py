from bisect import bisect_right
from typing import List

class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:

        prefix = []
        s = 0
        for t in tasks:
            s += t
            prefix.append(s)

        total = prefix[-1]
        processed = 0
        n = len(tasks)
        ans = []

        for shift in shifts:
            processed += shift

            if processed >= total:
                ans.append(0)
                processed = 0
            else:
                idx = bisect_right(prefix, processed)
                ans.append(n - idx)

        return ans