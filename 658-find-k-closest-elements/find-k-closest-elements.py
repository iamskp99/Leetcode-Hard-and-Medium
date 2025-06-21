from collections import deque
from bisect import bisect_left
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ind = bisect_left(arr,x)
        n = len(arr)
        ans = deque([])
        if ind != n and arr[ind] == x:
            ans.append(arr[ind])
            i = ind-1
            j = ind+1
        else:
            i = ind-1
            j = ind

        while (i > -1 or j < n) and len(ans) < k:
            if i == -1:
                ans.append(arr[j])
                j += 1
                continue

            if j == n:
                ans.appendleft(arr[i])
                i -= 1
                continue

            if abs(arr[i]-x) <= abs(arr[j]-x):
                ans.appendleft(arr[i])
                i -= 1
            else:
                ans.append(arr[j])
                j += 1

        return list(ans)